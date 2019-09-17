from flask import jsonify, render_template, redirect, url_for, request
from flask_login import login_required, current_user


from app.models.alert import Alert
from app.models.base import db
from app.models.user import User
from app.models.video import Video
from app.view_models.myalert import cut_alert
from app.view_models.myvideo import Myvideo
from app.web import web


@web.route('/getalert')
@login_required
def getalert():
    user=User.query.filter_by(id=current_user.id).first()
    alertnum=user.alertNumber
    if alertnum != 0 :
       alert=Alert.query.filter_by(userid=current_user.id).all()
       alerts=cut_alert(alert)
       return jsonify({
           'alerts':alerts,
           'alertnum':alertnum
       })
    return jsonify({
        'alertnum':0,
        'alertmessage':"you don't have alert now"
    })

@web.route('/processalert')
@login_required
def processalert():

    id=current_user.id
    video = Myvideo()
    videos = Video.query.filter_by(uid=id).all()
    video.cut_data(videos)
    try:
       alert=Alert.query.filter_by(userid=id).all()
       if alert:
           user = User.query.filter_by(id=id).first()
           user.alertNumber = 0
           db.session.add(user)
           for i in range(len(alert)):
               db.session.delete(alert[i])
           db.session.commit()

    except Exception as e:
       db.session.rollback()
       raise e

    return render_template('video.html',video=video.my_video)

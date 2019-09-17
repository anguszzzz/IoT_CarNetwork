import os
import stat
import time

from flask import jsonify, request, json, send_from_directory, redirect, url_for, send_file
from flask_login import current_user, login_required



from app.forms.videoForm import videoForm
from app.models.alert import Alert
from app.models.base import db
from app.models.user import User
from app.models.vehicles import Vehicles
from app.models.video import Video
from app.web import web


@web.route('/upload/<vehiclePlate>',methods=['POST','GET'])
def upload(vehiclePlate):
    vehicle=Vehicles.query.filter_by(vehiclePlate=vehiclePlate).first()
    path=vehicle.videos
    video=Video()
    alert=Alert()
    apikey=request.headers.get('Apikey')
    if vehicle and vehicle.apiKey ==apikey:
        os.chmod(path, stat.S_IWOTH)
        if request.method == 'POST':
            file = request.files['files']
            if file :
                try:
                   filename=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())+ '.mp4'
                   video.carPlate=vehiclePlate
                   video.path=path+"/"+filename
                   video.uploadDate=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
                   video.videoName=filename
                   file.save(path+"/"+filename)
                   message = " a new Alert Video uploads at" + video.uploadDate
                   alert.userid = vehicle.uid
                   alert.Plate = vehicle.vehiclePlate
                   alert.message = message
                   vehicle.videoNumber +=1
                   user=User.query.filter_by(id=vehicle.id).first()
                   video.uid =user.id
                   user.alertNumber += 1
                   db.session.add(user)
                   db.session.add(vehicle)
                   db.session.add(alert)
                   db.session.add(video)
                   db.session.commit()
                   return jsonify("successfully upload"),redirect(url_for('web.detection',videoname=video.videoName))
                except Exception as e:
                    db.session.rollback()
                    raise e

    return jsonify("Failure")

@web.route('/uploads/<vehiclePlate>/<videoName>',methods=['POST','GET'])
@login_required
def video(videoName,vehiclePlate):
    video=Video.query.filter_by(videoName=videoName).first()
    if video:
       vehicle=Vehicles.query.filter_by(vehiclePlate=vehiclePlate).first()
       path=vehicle.videos
       filename=video.videoName
       return send_from_directory(path,filename)
    else:
      path='C:/Users/leon/Desktop/IoTweb/app/uploads/'+vehiclePlate
      filename=videoName
      return send_from_directory(path,filename)

@web.route('/deletevideo',methods=['GET'])
@login_required
def deletevideo():
   form=videoForm(request.args)
   if form.validate():
       try:
           videoname=form.data['videoname']
           video=Video.query.filter_by(videoName=videoname).first()
           vehicle=Vehicles.query.filter_by(vehiclePlate=video.carPlate).first()
           vehicle.videoNumber -=1
           db.session.add(vehicle)
           db.session.delete(video)
           db.session.commit()
           return redirect(url_for('web.cardetail',vehiclePlate=vehicle.vehiclePlate))
       except Exception as e :
           db.session.rollback()
           raise e

   return redirect(url_for('web.carinfo'))


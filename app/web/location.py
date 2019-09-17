from flask import jsonify, render_template

from app.web import web


locations={
    'latitude' : 51.5421217,
    'longitude' :  -0.0174411,
}

@web.route('/map')
def map():
     return render_template('map.html')


@web.route('/getlocation')
def getlocation():
    return jsonify(locations)



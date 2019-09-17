from flask import  jsonify


from app.web import web

@web.route('/chart')
def chart():
    return jsonify(1)
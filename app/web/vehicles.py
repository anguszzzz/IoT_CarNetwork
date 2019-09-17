
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user

from app.forms.RegicarForm import RegicarForm, DeletecarForm
from app.libs.http import Http

from app.libs.makedir import mkdir
from app.models.base import db
from app.models.vehicles import Vehicles
from app.models.video import Video
from app.view_models.mycars import mycars
from app.view_models.myvideo import Myvideo
from app.web import web
import time

@web.route('/')
@login_required
def index():
   uid=current_user.id
   my_vehicle = mycars()
   vehiclenumber=current_user.vehicleNumber
   if vehiclenumber != 0:
       vehicles=Vehicles.query.filter_by(uid=uid).all()
       my_vehicle.cut_data(vehicles)
   else:
      my_vehicle.my_car ="None"
   data={
      'id':uid,
      'vehiclenumber':vehiclenumber,
      'vehicles':my_vehicle.my_car,

   }
   return render_template('homepage.html',data=data)


@web.route('/regicar',methods=['POST','GET'])
@login_required
def regicar():
  form = RegicarForm(request.form)
  if request.method == 'POST' and form.validate():
     try:
       path='C:/Users/leon/Desktop/IoTweb/app/uploads/' +form.data['vehiclePlate']
       if mkdir(path) :
          vehicle = Vehicles()
          vehicle.registerDate=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
          vehicle.Gennerate_apiKey(form.data['vehiclePlate'])
          vehicle.uid=current_user.id
          vehicle.set_attrs(form.data)
          vehicle.videos=path
          current_user.vehicleNumber +=1
          db.session.add(vehicle)
          db.session.commit()
          return redirect(url_for('web.carinfo'))
     except Exception as e:
         db.session.rollback()
         raise e

  return render_template('registerCar.html',form=form)


@web.route('/carinfo')
@login_required
def carinfo():
   my_vehicle=mycars()

   if current_user.vehicleNumber !=0:
      vehicles = Vehicles.query.filter_by(uid=current_user.id).all()
      my_vehicle.cut_data(vehicles)
   else:
      flash('Please register your car first!')
   data={
      'vehiclenumber':current_user.vehicleNumber,
      'vehicles':my_vehicle.my_car,

   }
   return render_template('carinfo.html',data=data)


@web.route('/<vehiclePlate>')
@login_required
def cardetail(vehiclePlate):
   my_vehicle=mycars()
   vehicle=Vehicles.query.filter_by(vehiclePlate=vehiclePlate).first()
   my_vehicle.cut_single(vehicle)
   video=Myvideo()
   videos=Video.query.filter_by(carPlate=vehiclePlate).all()
   video.cut_data(videos)


   return render_template('car.html',data=my_vehicle.my_car,video=video.my_video)



@web.route('/deletecar',methods=['GET'])
@login_required
def deletecar():
   form=DeletecarForm(request.args)
   if form.validate():
       try:
           vehiclePlate=form.data['vehiclePlate']
           vehicles=Vehicles.query.filter_by(vehiclePlate=vehiclePlate).first()


           current_user.vehicleNumber -= 1
           db.session.delete(vehicles)
           db.session.commit()
           return redirect(url_for('web.carinfo'))
       except Exception as e :
           db.session.rollback()
           raise e

   return redirect(url_for('web.carinfo'))


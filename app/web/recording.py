import os
import time

from flask import jsonify, render_template, request, send_from_directory
from flask_login import login_required, current_user
from imageai.Detection import VideoObjectDetection

from app.forms.videoForm import videoForm, detectForm
from app.models.vehicles import Vehicles
from app.models.video import Video
from app.view_models.myvideo import Myvideo
from app.web import web
import os
from app.libs.convert import convert
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

@web.route('/recording')
@login_required
def rec():
    id=current_user.id
    videos=Video.query.filter_by(uid=id).all()
    video = Myvideo()
    video.cut_data(videos)


    return render_template('/video.html',video=video.my_video)

@web.route('/detection')
@login_required
def detection():
    form = videoForm(request.args)
    if form.validate():
        video = Video.query.filter_by(videoName=form.data['videoname']).first()
        vehiclePlate=video.carPlate
        vehicle=Vehicles.query.filter_by(vehiclePlate=vehiclePlate).first()
        path=vehicle.videos
        return jsonify({
             'inputpath':path,
            'outputpath':video.path,
            'videoname':video.videoName,
            'vehiclePlate':vehicle.vehiclePlate
        })

    return jsonify('error')
@web.route('/getdetect')
@login_required
def detected():
    form=detectForm(request.args)
    if form.validate():
       input_path=form.data['inputpath']
       output_path= form.data['outputpath']
       videoName=form.data['videoname']
       try:
          detector = VideoObjectDetection()
          start = time.time()
          detector.setModelTypeAsRetinaNet()
          detector.setModelPath(os.path.join(input_path, "resnet50_coco_best_v2.0.1.h5"))
          detector.loadModel(detection_speed="fastest")
          video_path = detector.detectObjectsFromVideo(input_file_path=output_path,
                                                       output_file_path=os.path.join(input_path, "detected"+videoName),
                                                       frames_per_second=10, log_progress=True)

          convert(video_path, input_path+"/dectected"+videoName)
          end = time.time()
          processtime = end - start
          return jsonify({
           'video_path':video_path,
           'processtime':processtime
          })
       except Exception as e:
           raise e
    return jsonify({'error':'no correct form'})

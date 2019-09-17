from flask import Blueprint

web=Blueprint('web',__name__)

from app.web import tfl
from app.web import location
from app.web import vehicles
from app.web import Chart
from app.web import recording
from app.web import video
from app.web import alert
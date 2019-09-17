
import multiprocessing
import subprocess
import sys

inputpath='C:\\Users\\leon\\Desktop\\IoTweb\\app\\uploads\\710\\2018-08-20-00-07-04.mp4'
outputpath='C:\\Users\\leon\\Desktop\\IoTweb\\app\\uploads\\710\\detect2018-08-20-00-07-04.mp4'



def convert(inputpath,outputpath):

    cmd='ffmpeg -i "%s" -vcodec libx264 -preset fast -profile:v main -acodec aac  "%s" -hide_banner' %(inputpath,outputpath)
    return subprocess.call(cmd,shell=True)


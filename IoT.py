
from app import create_app


app =create_app()

inputpath='C:\\Users\\leon\\Desktop\\IoTweb\\app\\uploads\\710\\2018-08-20-00-07-04.mp4'
outputpath='C:\\Users\\leon\\Desktop\\IoTweb\\app\\uploads\\710\\detect2018-08-20-00-07-04.mp4'
if __name__ =='__main__':

    app.run(host='0.0.0.0',port='6060',threaded=True)


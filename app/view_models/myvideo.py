class Myvideo():
    def __init__(self):

        self.my_video=[]

    def cut_data(self, video):
        my_video = []
        for i in range(len(video)):
            temp = {
                'carPlate': video[i].carPlate,
                'uploadDate': video[i].uploadDate,
                'path':video[i].path,
                'videoName': video[i].videoName
            }
            my_video.append(temp)
        self.my_video = my_video
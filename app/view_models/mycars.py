
class mycars:
    def __init__(self):
        self.my_car=[]
    def cut_data(self,vehicles):
        my_car=[]
        for vehicle in range(len(vehicles)):
            temp={
                'vehiclePlate':vehicles[vehicle].vehiclePlate,
                'registerDate':vehicles[vehicle].registerDate,
                'brand':vehicles[vehicle].brand,
                'type':vehicles[vehicle].type,
                'email':vehicles[vehicle].email,
                'uid':vehicles[vehicle].uid,
                'status':vehicles[vehicle].status,
                'apiKey':vehicles[vehicle].apiKey
            }
            my_car.append(temp)
        self.my_car=my_car
    def cut_single(self,vehicle):
        if vehicle != None:
           my_car=[]
           temp = {
               'vehiclePlate': vehicle.vehiclePlate,
               'registerDate': vehicle.registerDate,
               'brand': vehicle.brand,
               'type': vehicle.type,
               'email': vehicle.email,
               'uid': vehicle.uid,
               'status': vehicle.status,
               'apiKey': vehicle.apiKey,
               'video':vehicle.videos,
           }
           my_car.append(temp)
           self.my_car=my_car
     



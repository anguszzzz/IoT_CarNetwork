
def cut_alert(alert):
    for i in range(len(alert)):
        my_alert = []
        temp = {
            'vehiclePlate': alert[i].Plate,
            'message': alert[i].message,
            'id':alert[i].id
        }
        my_alert.append(temp)
    return my_alert
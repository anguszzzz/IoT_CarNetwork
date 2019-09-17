from app.libs.http import Http

class Location:
    url1="https://maps.googleapis.com/maps/api/geocode/json?latlng={}&key=AIzaSyB3ulTQCxzq5RTXxvXlID2FRg3Qgvpzlbo"
    url2="https://maps.googleapis.com/maps/api/streetview?location={}&size=456x456&key=AIzaSyB3ulTQCxzq5RTXxvXlID2FRg3Qgvpzlbo"


    def __init__(self):
        self.locations=[]
        self.total=0




    def getLocation(self,Latlng):
        url=self.url1.format(Latlng)
        result=Http.get(url)
        self._fill(result)
        url1=self.url2.format(Latlng)
        result1=Http.getPicture(url1) 
        self._fill(result)
        self.view=result1

    

    def _fill(self,data):
       results=data['results']

       address_components=results[0]
       geometry=address_components['geometry']
       #bounds=geometry['bounds']
       #self.northeast=bounds['northeast']
       #self.southwest=bounds['southwest']
       self.place_id=address_components['place_id']

       self.types=address_components['types']
       self.formatname=address_components['formatted_address']









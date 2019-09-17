from macpath import join


class Tfl:
     def __init__(self):
         self.tfls=[]
         self.total=0


     def _cut_tfl_data(self,data):
         self.total =data['total']
         data=data['matches']
         self.tfls=[]

         for i in range(len(data)):
             temp=data[i]

             str=','.join(temp['highlights'])

             tfl={
                 'highlights':str,
                 #'name':temp['name'],
                 'id':temp['id'],
                 'score':temp['score'],
                 'url':temp['url'],
             }
             self.tfls.append(tfl)


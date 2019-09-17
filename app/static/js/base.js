var alertid=[];
var vehiclePlate=[];
function check(){
        $.ajax({
            type:"GET",
            url:"/getalert",
            dataType:"json",
            success:function(data){
                if(data.alertnum!=0){

                     document.getElementById("alertnum").innerHTML=data.alertnum;
                     alertsdata=data['alerts'];
                      for(i=0;i<data.alertnum;i++){
                       document.getElementById("alertmessage").innerHTML="your "+alertsdata[i].vehiclePlate+"car"+","+alertsdata[i].message;
                       alertid[i]=alertsdata[i].id;
                       vehiclePlate[i]=alertsdata[i].vehiclePlate;
                }}


                else{
                    document.getElementById("alertnum").innerHTML=data.alertnum;
                    document.getElementById("alertmessage").innerHTML=data.alertmessage;

                }
            },

        });
    }


    window.setInterval(check,10000000);

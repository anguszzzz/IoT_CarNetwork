
$(function() {
    $('#OriginMap').click(function () {
        $.ajax({
            url: '/getlocation',
            success: function (data) {
               latitude = data['latitude'] ;
               longtitude = data['longitude'];
               initMap(latitude,longtitude );


            }
        })

    })

})
$(function() {
    $('#StreetView').click(function () {
        $.ajax({
            url: '/getlocation',
            success: function (data) {
               latitude = data['latitude'] ;
               longtitude = data['longitude'];
              initStreet(latitude,longtitude );


            }
        })

    })

})


function initMap(latitude,longtitude) {
    // var myCenter = new google.maps.LatLng(51.508742, -0.120850);
    // var boolean = false;


    var myCenter = new google.maps.LatLng(latitude, longtitude);

    var mapProp = {
        center: myCenter,
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("MapOrStreetView"), mapProp);

    var marker = new google.maps.Marker({
        position: myCenter,
    });
    marker.setMap(map);
    var infowindow = new google.maps.InfoWindow({
        content: "Accident happen!"
    });

    infowindow.open(map, marker);
    google.maps.event.addListener(marker, 'click', function () {
        map.setZoom(20);
        map.setCenter(marker.getPosition());
    });

    // if(boolean == true){
    //
    // }
}

function initStreet(latitude,longtitude){



    var myCenter = new google.maps.LatLng(latitude, longtitude);

    var mapProp = {
        center: myCenter,
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("MapOrStreetView"), myCenter);

    var panorama = new google.maps.StreetViewPanorama(
        document.getElementById('MapOrStreetView'), {
            position: {lat: latitude,lng: longtitude},
            pov: {
                heading: 0,
                pitch: 10
            }
        });
    map.setStreetView(panorama);
}

google.maps.event.addDomListener(window, 'load', initMap);
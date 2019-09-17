function initialize() {
    // var myCenter = new google.maps.LatLng(51.508742, -0.120850);
    var latitude = 51.508742;
    var longitude = -0.120850;
    //var temp1=document.getElementById("longitude").value;
    //var temp2=document.getElementById("latitude").value;
    //if (temp1 != null){
    //longitude = parseFloat(document.getElementById("longitude").value);
    //}
    //if( temp2 != null ){
    //latitude = parseFloat(document.getElementById("latitude").value);
    //}
    var myCenter = new google.maps.LatLng(latitude, longitude);

    var mapProp = {
        center: myCenter,
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);


    var panorama = new google.maps.StreetViewPanorama(
        document.getElementById('streetView'), {
            position: {lat: latitude,lng: longitude},
            pov: {
                heading: 0,
                pitch: 10
            }
        });
    map.setStreetView(panorama);


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
}

    google.maps.event.addDomListener(window, 'load', initialize);
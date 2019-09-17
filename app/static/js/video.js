var options=$("#videoname option:selected");
var videoname=options.text();
var url='/detection?videoname=' + videoname


$(function() {
    $('#return_path').click(function () {
        $.ajax({
        url: url,
        success: function (data) {
            inputpath = data['inputpath'];
            outputpath = data['outputpath'];
            videoName = data['videoname'];
            carPlate=data['vehiclePlate'];
            detect(inputpath,outputpath,videoName,carPlate)
        }
    })

        }
    )

})

function detect(inputpath,outputpath,videoname,carPlate) {
    $.ajax({
        url: '/getdetect?inputpath='+inputpath+'&'+'outputpath='+outputpath+'&'+'videoname='+videoname,
        success: function (data) {
            initvideo(carPlate)

        }


    })
}

function initvideo(carPlate) {
     var src='/uploads/'+carPlate+'/detected'+videoname
    var sourceDom = $("<source src=\""+ src +"\" type='video/mp4'>");
    $("#video-box video").append(sourceDom);
    $("#video-box").load();
    $("#video-box").show();
    $("#video-box")[0].play();}


var src='/uploads/710/detected'+videoname
var sourceDom = $("<source src=\""+ src +"\" type='video/mp4'>");
$("#video-box ").append(sourceDom);
$("#video-box").load();
$("#video-box").show();
$("#video-box")[0].play()


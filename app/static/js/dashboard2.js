'use strict'
$(document).ready(function() {
    $('.counter').counterUp({
        delay: 60,
        time: 1000
    });


    if ($('#chart_1').length > 0) {
        var ctx1 = document.getElementById("chart_1").getContext("2d");
        var data1 = {

            // TODO: All those data should be loaded from the server side

            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                    label: "Leon",
                    backgroundColor: "rgba(238, 206, 83, 0.9)",

                    pointHighlightStroke: "rgba(60,184,120,1)",
                    data: [800, 280, 500, 120, 200, 160, 400]
                },
                {
                    label: "Anguse",
                    backgroundColor: "rgba(93, 159, 247, 0.9)",

                    pointBackgroundColor: "rgba(252,176,59,0.4)",
                    data: [0, 1, 2, 3, 4, 5, 6],
                },
                {
                    label: "Zell",
                    backgroundColor: "rgba(219, 80, 74, 0.86)",

                    pointBackgroundColor: "rgba(252,176,59,0.4)",
                    data: [200, 600, 100, 190, 560, 270, 100],
                }
            ]
        };

        var areaChart = new Chart(ctx1, {
            type: "line",
            data: data1,

            options: {
                tooltip: {
                    mode: "label"
                },
                elements: {
                    point: {
                        hitRadius: 10
                    }
                },

                scales: {
                    yAxes: [{
                        stacked: false,
                        gridLines: {
                            color: "#eee",
                        },
                        ticks: {
                            fontColor: "#2f2c2c"
                        }
                    }],
                    xAxes: [{
                        stacked: false,
                        gridLines: {
                            color: "#eee",
                        },
                        ticks: {
                            fontColor: "#2f2c2c"
                        }
                    }]
                },
                animation: {
                    duration: 3000
                },
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    display: false,
                },
                tooltips: {
                    backgroundColor: 'rgba(47,44,44,.9)',
                    cornerRadius: 0,
                }
            }
        });
    }


});

//dashboard page loading segment trigger
$(".refreshing").on("click", function() {
    $(".dimmer").addClass("active").delay(1500).queue(function() {
        $(".dimmer").removeClass("active").dequeue();
    });
});
//dashboard page loading segment trigger

//Pace Loading (On Navbar) Function
function paceLoading() {
    var paceOptions = {
        restartOnRequestAfter: false
    };

    $(document).ajaxStart(function() {
        Pace.restart();
    });
}
//Pace Loading (On Navbar) Function


'use strict';

$(document).ready(function() {

    // Make some random data for the Chart
    var d1 = [];
    for (var i = 0; i <= 10; i += 1) {
        d1.push([i, parseInt(Math.random() * 30)]);
    }
    var d2 = [];
    for (var i = 0; i <= 25; i += 4) {
        d2.push([i, parseInt(Math.random() * 30)]);
    }
    var d3 = [];
    for (var i = 0; i <= 10; i += 1) {
        d3.push([i, parseInt(Math.random() * 30)]);
    }

    // Chart Options
    var options = {
        series: {
            shadowSize: 0,
            curvedLines: {
                apply: true,
                active: true,
                monotonicFit: true
            },
            lines: {
                show: false,
                lineWidth: 0
            }
        },
        grid: {
            borderWidth: 0,
            labelMargin: 10,
            hoverable: true,
            clickable: true,
            mouseActiveRadius: 6

        },
        xaxis: {
            tickDecimals: 0,
            ticks: false
        },

        yaxis: {
            tickDecimals: 0,
            ticks: false
        },

        legend: {
            show: false
        }
    };

    // Let's create the chart
    if ($("#chart-curved-line")[0]) {
        $.plot($("#chart-curved-line"), [{
            data: d1,
            lines: {
                show: true,
                fill: 0.98
            },
            label: 'Product 1',
            stack: true,
            color: '#52489C'
        }, {
            data: d3,
            lines: {
                show: true,
                fill: 0.98
            },
            label: 'Product 2',
            stack: true,
            color: '#59C3C3'
        }], options);
    }

    if ($("#chart-past-days")[0]) {
        $.plot($("#chart-past-days"), [{
            data: d2,
            lines: {
                show: true,
                fill: 1,
            },
            label: 'Product 1',
            stack: true,
            color: '#35424b'
        }], options);
    }

    // Tooltips for Flot Charts
    if ($('.flot-chart')[0]) {
        $('.flot-chart').on('plothover', function(event, pos, item) {
            if (item) {
                var x = item.datapoint[0].toFixed(2),
                    y = item.datapoint[1].toFixed(2);
                $('.flot-tooltip').html(item.series.label + ' of ' + x + ' = ' + y).css({ top: item.pageY + 5, left: item.pageX + 5 }).show();
            } else {
                $('.flot-tooltip').hide();
            }
        });

        $('<div class="flot-tooltip"></div>').appendTo('body');
    }

    $('#sidebar_progress1').progress({
        duration: 200,
        total: 200,
        percent: 45
    });
    $('#sidebar_progress2').progress({
        duration: 200,
        total: 200,
        percent: 68
    });
    $('#sidebar_progress3').progress({
        duration: 200,
        total: 200,
        percent: 36
    });
});

$(".modalactionone").on("click", function () {
    $(".ui.actionmodal").modal({
        closable: false,
        onDeny: function () {
            window.alert("OOooopps! You must read this..");
            return false;
        },
        onApprove: function () {
            window.location.href = "/regicar";
        }
    }).modal("show");
});
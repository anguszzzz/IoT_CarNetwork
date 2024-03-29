Highcharts.setOptions({
	chart: {
		type: 'solidgauge'
	},
	title: null,
	pane: {
		center: ['50%', '85%'],
		size: '140%',
		startAngle: -90,
		endAngle: 90,
		background: {
			backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
			innerRadius: '60%',
			outerRadius: '100%',
			shape: 'arc'
		}
	},
	tooltip: {
		enabled: false
	},
	yAxis: {
		stops: [
			[0.1, '#55BF3B'], // green
			[0.5, '#DDDF0D'], // yellow
			[0.9, '#DF5353'] // red
		],
		lineWidth: 0,
		minorTickInterval: null,
		tickPixelInterval: 400,
		tickWidth: 0,
		title: {
			y: -70
		},
		labels: {
			y: 16
		}
	},
	plotOptions: {
		solidgauge: {
			dataLabels: {
				y: 5,
				borderWidth: 0,
				useHTML: true
			}
		}
	}
});
// 速度仪表
var chart1 = Highcharts.chart('container-speed', {
	yAxis: {
		min: 0,
		max: 200,
		title: {
			text: '速度'
		}
	},
	credits: {
		enabled: false
	},
	series: [{
		name: '速度',
		data: [80],
		dataLabels: {
			format: '<div style="text-align:center"><span style="font-size:25px;color:' +
			((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
			'<span style="font-size:12px;color:silver">km/h</span></div>'
		},
		tooltip: {
			valueSuffix: ' km/h'
		}
	}]
});
// 转速仪表
var chart2 = Highcharts.chart('container-rpm', {
	yAxis: {
		min: 0,
		max: 5,
		title: {
			text: 'RPM'
		}
	},
	series: [{
		name: 'RPM',
		data: [1],
		dataLabels: {
			format: '<div style="text-align:center"><span style="font-size:25px;color:' +
			((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y:.1f}</span><br/>' +
			'<span style="font-size:12px;color:silver">* 1000 / min</span></div>'
		},
		tooltip: {
			valueSuffix: ' revolutions/min'
		}
	}]
});
// 定时刷新数据
setInterval(function () {
	var point,
		newVal,
		inc;
	if (chart1) {
		point = chart1.series[0].points[0];
		inc = Math.round((Math.random() - 0.5) * 100);
		newVal = point.y + inc;
		if (newVal < 0 || newVal > 200) {
			newVal = point.y - inc;
		}
		point.update(newVal);
	}
	if (chart2) {
		point = chart2.series[0].points[0];
		inc = Math.random() - 0.5;
		newVal = point.y + inc;
		if (newVal < 0 || newVal > 5) {
			newVal = point.y - inc;
		}
		point.update(newVal);
	}
}, 2000);

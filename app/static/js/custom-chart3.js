'use strict'

var option = {
    title: {
        text: 'Data of your vehicle'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ['Speed', 'Acceleration', 'Distance between barrier']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: 'Speed',
            type: 'line',
            stack: '',
            data: [120, 122, 101, 110, 100, 90, 100]
        },
        {
            name: 'Acceleration',
            type: 'line',
            stack: '',
            data: [2, 1, 1, 24, 0, 30, 30]
        },
        {
            name: 'Distance between barrier',
            type: 'line',
            stack: '',
            data: [10, 22, 21, 15, 10, 30, 10]
        }
    ]
};





var colors = ['#5793f3', '#d14a61', '#675bba'];





// 基于准备好的dom，初始化echarts实例
var myChart_axes = echarts.init(document.getElementById('main-line'));

// 使用刚指定的配置项和数据显示图表。
myChart_axes.setOption(option);





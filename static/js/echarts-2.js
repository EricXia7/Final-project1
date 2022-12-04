var lineChart = echarts.init(document.getElementById('lineChart'));
//Line chart sets parameters
var line_option = {
    title: {
        text: 'Number of film genres in different years',
        left: 'center'
    },
    tooltip: { //Prompt Message
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: { //icon
        data: ['Comedy', 'Drama', 'Horror', 'Action'],
        left:"right",
    },
    grid: {  //Arrangement of position
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [  //x axis
        {
            type: 'category',
            name: "year",
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        }
    ],
    yAxis: [ //y axis
        {
            type: 'value',
            name: "number of films",
        }
    ],
    series: [  //data
        {
            name: 'Comedy',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [120, 132, 101, 134, 90, 230, 210]
        },
        {
            name: 'Drama',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [220, 182, 191, 234, 290, 330, 310]
        },
        {
            name: 'Horror',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [150, 232, 201, 154, 190, 330, 410]
        },
        {
            name: 'Action',
            type: 'line',
            stack: 'Total',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: [320, 332, 301, 334, 390, 330, 320]
        },

    ]
};



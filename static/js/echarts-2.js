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
        data: ['Drama','Comedy', 'crime','Action','romance'],
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
            name: 'Drama',
            type: 'line',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: []
        },
        {
            name: 'Comedy',
            type: 'line',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: []
        },
        {
            name: 'crime',
            type: 'line',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: []
        },
        {
            name: 'Action',
            type: 'line',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: []
        },
        {
            name: 'romance',
            type: 'line',
            areaStyle: {},
            emphasis: {
                focus: 'series'
            },
            data: []
        },
         


    ]
};



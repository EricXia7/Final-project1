var pieChart = echarts.init(document.getElementById('pieChart'));
//Pie chart parameters


var pie_option = {
    title: {
        text: 'Genre',
        subtext: 'Fake Data',
        left: 'center'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        orient: 'vertical',
        left: 'right'
    },
    series: [
        {
            name: 'Type',
            type: 'pie',
            radius: '50%',
            data: [
                {value: 1048, name: 'Search Engine'},
                {value: 735, name: 'Direct'},
                {value: 580, name: 'Email'},
                {value: 484, name: 'Union Ads'},
                {value: 300, name: 'Video Ads'}
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            },

        }
    ]
};


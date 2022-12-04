var girth = [8.3, 8.6, 8.8, 10.5, 10.7, 10.8, 11.0, 11.0, 11.1, 11.2, 11.3, 11.4, 11.4, 11.7, 12.0, 12.9];
function histChart() {

    $.ajaxSetup({async: false});
    $.ajax({
        url: '/echarts1',
        success: function (res) {
            girth = res.data
        },
        error: function (xhr, type, errorThrown) {
        }
    });

    set_hist()
}

function set_hist() {

     var histChart = echarts.init(document.getElementById('histChart'));

    var bins = ecStat.histogram(girth, 'scott');


    var interval;

    var min = Infinity;
    var max = -Infinity;

    var data = echarts.util.map(bins.data, function (item, index) {

        var x0 = bins.bins[index].x0;

        var x1 = bins.bins[index].x1;
        interval = (x1 - x0).toFixed(2);

        min = Math.min(min, x0);
        max = Math.max(max, x1);

        return [x0, x1, item[1]];
    });

    function renderItem(params, api) {

        var yValue = api.value(2);
        var start = api.coord([api.value(0), yValue]);
        var size = api.size([api.value(1) - api.value(0), yValue]);
        var style = api.style();

        return {
            type: 'rect',
            shape: {
                x: start[0],
                y: start[1],
                width: size[0],
                height: size[1]
            },
            style: style
        };
    }
    var bar_option = {
        title: {
            text: 'Rating distribution',
            left: 'center',
            top: 10
        },
        color: ['rgb(25, 183, 207)'],
       grid: {
          top: "8%",
          left: "3%",
          right: "3%",
          bottom: "3%",
          containLabel: true
        },

        tooltip: {
            trigger: 'item'
        },
        xAxis: [{
            type: 'value',
            name:"Rating",
            min: min,
            max: max,
            interval: 0.1,

        }],
        yAxis: [{
            type: 'value',
            name:"Number of movies",
        }],
        series: [{
            name: 'Number of movies',
            type: 'custom',
            renderItem: renderItem, 
            barWidth:30,
            encode: {
                x: [0, 1],
                y: 2,
                tooltip: 2,
                label: 2
            },
            data: data,
             itemStyle: {
                normal: {
                    label: {
                        show: true
                        position: 'top', 
                        textStyle: { 
                            color: 'blue',
                            fontSize: 16
                        }
                    }
                }
            },
        }]
    };


    histChart.setOption(bar_option);
     window.addEventListener("resize", function () {
        histChart.resize();
    });

    // var girth = [1,2,3,4,4,5,55];
}












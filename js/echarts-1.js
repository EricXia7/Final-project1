var girth = [8.3, 8.6, 8.8, 10.5, 10.7, 10.8, 11.0, 11.0, 11.1, 11.2, 11.3, 11.4, 11.4, 11.7, 12.0, 12.9];
//直方图初始化函数，
function histChart() {
//发送请求，赋值
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

//直方图参数
function set_hist() {

     var histChart = echarts.init(document.getElementById('histChart'));
    // See https://github.com/ecomfe/echarts-stat
    var bins = ecStat.histogram(girth, 'scott');

    // 柱子间间隔的刻度
    var interval;

    var min = Infinity;
    var max = -Infinity;

    var data = echarts.util.map(bins.data, function (item, index) {
        // 左刻度
        var x0 = bins.bins[index].x0;
        // 右刻度
        var x1 = bins.bins[index].x1;
        interval = (x1 - x0).toFixed(2);
        // 获得数据集中最值
        min = Math.min(min, x0);
        max = Math.max(max, x1);
        // item[0]代表刻度的中间值，item[1]代表出现的次数
        return [x0, x1, item[1]];
    });
     // 自定义渲染效果
    function renderItem(params, api) {
        // 这个根据自己的需求适当调节
        var yValue = api.value(2);
        var start = api.coord([api.value(0), yValue]);
        var size = api.size([api.value(1) - api.value(0), yValue]);
        var style = api.style();

        return {
            // 矩形及配置
            type: 'rect',
            shape: {
                x: start[0],
                y: start[1],
                width: size[0],  //图形宽度
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
            type: 'custom',  //自定义
            renderItem: renderItem,  //各种值
            barWidth:30,
            encode: {
                // 表示将data中的data[0]和data[1]映射到x轴
                x: [0, 1],
                // 表示将data中的data[2]映射到y轴
                y: 2,
                // 表示将data中的data[2]映射到tooltip
                tooltip: 2,
                // 表示将data中的data[2]映射到label
                label: 2
            },
            data: data,
             itemStyle: {
                normal: {
                    label: {
                        show: true, //开启显示
                        position: 'top', //在上方显示
                        textStyle: { //数值样式
                            color: 'blue',
                            fontSize: 16
                        }
                    }
                }
            },
        }]
    };











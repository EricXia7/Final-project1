//页面加载完执行函数
$(function () {

    histChart();
    line_cart();
    pie_cart();
});

//折线图函数，初始化折线图，发送ajax请求获取数据，赋值
function line_cart() {
    $.ajax({
        url: '/echarts2',
        success: function (res) {
            line_option.series[0].data = res.data1;
            line_option.series[1].data = res.data2;
            line_option.series[2].data = res.data3;
            line_option.series[3].data = res.data4;
            line_option.xAxis[0].data = res.years;
            lineChart.setOption(line_option);
        },
        error: function (xhr, type, errorThrown) {
        }
    });

    window.addEventListener("resize", function () {
        lineChart.resize();
    });
}
//饼状图函数，初始化折线图，发送ajax请求获取数据，赋值
function pie_cart() {
     $.ajax({
        url: '/echarts3',
        success: function (res) {
            pie_option.series[0].data = res.data;
              pieChart.setOption(pie_option);
        },
        error: function (xhr, type, errorThrown) {
        }
    });

    window.addEventListener("resize", function () {
        pieChart.resize();
    });
}
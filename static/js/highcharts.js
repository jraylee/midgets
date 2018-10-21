var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
        url: '/live-data',
        success: function(points) {
            var series = chart.series[0],
                shift = series.data.length > 200; // shift if the series is
                                                 // longer than 20
//            console.log(points);
//            // add the point
//            for (i=0; i < points[0][0].length; i++) {
//                point = {x:points[0][0][i], y:points[1][0][i]};
//                console.log(point);
//                chart.series[0].addPoint(point, true, shift);
//            }
            // add the point
            chart.series[0].addPoint(points, true, shift);

            // call it again after one second
            setTimeout(requestData, 100);
        },
        cache: false
    });
}

$(document).ready(function() {
    console.log('hi');
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            animation: false,
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live random data'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000,
            title: {
                text: 'Time'
            }
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Volume',
                margin: 80
            },
            min: 0,
            max: 1000,
        },
        series: [{
            name: 'Random data',
            data: []
        }],
        plotOptions: {
            line: {
                animation: false,
            }
        }
    });
});
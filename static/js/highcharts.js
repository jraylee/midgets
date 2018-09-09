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
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20
            console.log(points);
            // add the point
//            for (i=0; i< point)
//            chart.series[0].addPoint(point, true, shift);

            // call it again after one second
//            setTimeout(requestData, 1000);
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
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live random data'
        },
        xAxis: {
            type: 'Time',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Volume',
                margin: 80
            }
        },
        series: [{
            name: 'Random data',
            data: []
        }]
    });
});
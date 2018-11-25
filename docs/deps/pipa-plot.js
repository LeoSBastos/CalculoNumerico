'use strict';

var layout = {
    dragmode: 'pan',
    yaxis: {
        scaleanchor: 'x'
    }
};

var options = {
    displayModeBar: true,
    scrollZoom: true,
    displaylogo: false,
    warn: false
};

var data = [];

function plot(chart) {
    data.push(chart);
    Plotly.newPlot('plot', data, layout, options);
    document.getElementById('loader').style.display = 'none'
    window.onresize = function () {
        Plotly.relayout('plot', {
            width: innerWidth,
            height: innerHeight,
        });
    };
}

function range() {
    var args = Array.from(arguments);
    return math.map(math.range.apply(this, math.map(args, function (x) {
        return math.bignumber(x);
    })), function (x) {
        return math.number(x);
    }).toArray();
}

var morrisDonut;
var morrisLine;
var morris;
function donutGraph(data){
  morrisDonut = Morris.Donut({
    element: 'donut',
    data: data,
    formatter: function (value, data) { 
    return value+' %'; 
    },
    colors: ['#c9302c', '#337ab7','#5cb85c','#f0ad4e']
  });
}

function lineGraph(data, color, labels){
  morrisLine = Morris.Line({
    element: 'line',
    parseTime: false,
    data: data,
    pointSize: 0,
    xkey: 'y',
    ykeys: ['a','b','c','d'],
    labels: labels,
    lineColors: colors,
    resize: true,
    redraw: true,
    xLabels: 'seconds',
  });
}

function barGraph(data, color, labels){
  console.log("en barGraph")
  morris = Morris.Bar({
    element: 'graph',
    data: data,
    xkey: 'x',
    ykeys: ['y'],
    labels: labels,
    barColors: color,
    resize: true,
    redraw: false,
  });
}

function barGraph2(data, color, labels){
  morris2 = Morris.Bar({
    element: 'graph2',
    data: data,
    xkey: 'x',
    ykeys: ['y'],
    labels: labels,
    barColors: color
  });
}

  
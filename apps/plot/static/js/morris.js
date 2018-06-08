
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

function lineGraph(data){
  morrisLine = Morris.Line({
    element: 'line',
    parseTime: false,
    data: data,
    xkey: 'y',
    ykeys: ['a','b','c','d'],
    labels: ['Usuario 1', 'Usuario 2', 'Usuario 3', 'Usuario 4'],
    lineColors: ['#c9302c', '#337ab7','#5cb85c','#f0ad4e'],
    resize: true,
    redraw: true,
    xLabels: 'seconds',
  });
}

function barGraphMultiColor(data, labels){
  morrisColors = Morris.Bar({
    element: 'graph',
    data: data,
    xkey: 'x',
    ykeys: ['y'],
    labels: labels,
    barColors: function (row, series, type) {
    /*console.log("--> "+row.label, series, type);*/
    if(row.label == "Usuario 1") return "#c9302c";
    else if(row.label == "Usuario 2") return "#337ab7";
    else if(row.label == "Usuario 3") return "#5cb85c";
    else if(row.label == "Usuario 4") return "#f0ad4e";
    }
  });
}

function barGraph(data, color, labels){
  morris = Morris.Bar({
    element: 'graph',
    data: data,
    xkey: 'x',
    ykeys: ['y'],
    labels: labels,
    barColors: color
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

  
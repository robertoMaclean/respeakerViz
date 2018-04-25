
var morrisDonut;
var morrisLine;
var morris;
function donutGraph(data){
  morrisDonut = Morris.Donut({
    element: 'donut',
    data: data,
    colors: ['red', 'blue','green','yellow']
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
    resize: true,
    redraw: true,
    xLabels: 'seconds'
  });
}

function barGraph(data){
  morris = Morris.Bar({
    element: 'graph',
    data: data,
    xkey: 'x',
    ykeys: ['y'],
    labels: ['Duración']
  });
}
  


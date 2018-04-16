Morris.Bar({
  element: 'graph',
  data: [
    {x: '2011 Q1', y: 3},
    {x: '2011 Q2', y: 2},
    {x: '2011 Q3', y: 0},
    {x: '2011 Q4', y: 2}
  ],
  xkey: 'x',
  ykeys: ['y'],
  labels: ['Y']
}).on('click', function(i, row){
  console.log(i, row);
});
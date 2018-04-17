var morris = Morris.Bar({
  element: 'graph',
  data: [
    {x: '2011 Q1', y: 3},
    {x: '2011 Q2', y: 2},
    {x: '2011 Q3', y: 0},
    {x: '2011 Q4', y: 2}
  ],
  xkey: 'x',
  ykeys: ['y'],
  labels: ['Duración']
});

var morrisDonut = Morris.Donut({
  element: 'donut',
  data: [
    {label: "Download Sales", value: 12},
    {label: "In-Store Sales", value: 30},
    {label: "Mail-Order Sales", value: 20}
  ]
});


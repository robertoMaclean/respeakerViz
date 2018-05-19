function buble(){ 

  var svg = d4.select("svg"),
      diameter = +svg.attr("width"),
      g = svg.append("g").attr("transform", "translate(2,2)"),
      format = d4.format(",d");

  var pack = d4.pack()
      .size([diameter - 4, diameter - 4]);

  d4.json(user+'/flare.json', function(error, root) {
    if (error) throw error;

    root = d4.hierarchy(root)
        .sum(function(d) { return d.size; })
        .sort(function(a, b) { return b.value - a.value; });

    var node = g.selectAll(".node")
      .data(pack(root).descendants())
      .enter().append("g")
        .attr("class", function(d) { return d.children ? "node" : "leaf node"; })
        .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

    node.append("title")
        .text(function(d) { return d.data.name + "\n"; });

    node.append("circle")
        .attr("r", function(d) { return d.r; });

    node.filter(function(d) { return !d.children; }).append("text")
        .attr("dy", "0.3em")
        .text(function(d) { return d.data.name.substring(0, d.r / 3); });
  });
}

function relations(){
   var margin = {top: 90, right: 150, bottom: 90, left: 100},
      width =  2000 - margin.left - margin.right,
      height = 600 - margin.top - margin.bottom;

  function fx(d) { return d.gender; }
  function fy(d) { return d.group; }

  var x = d3.scale.ordinal()
      .rangePoints([5, width - 6]);

  var y = d3.scale.ordinal()
      .rangePoints([5, height - 6]);

  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("top");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

  var rollup = d3.rollup()
      .x(function(d) { return x(fx(d)); })
      .y(function(d) { return y(fy(d)); });
  
  var svg = d3.select("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  /*var svg = d3.select("svg"),
      diameter = +svg.attr("width"),
      g = svg.append("g").attr("transform", "translate(2,2)"),
      format = d3.format(",d");*/

  d3.json(user+"/relations", function(error, social) {
    if (error) throw error;
    console.log(social.nodes.length)
    x.domain(social.nodes.map(fx));
    y.domain(social.nodes.map(fy));
    var graph = rollup(social);
    svg.attr("width", 10000 + margin.left + margin.right)
    svg.selectAll(".link")
        .data(graph.links)
      .enter().append("path")
        .attr("class", "link")
        .attr("d", function(d) {
          var sx = d.source.x, sy = d.source.y,
              tx = d.target.x, ty = d.target.y,
              dx = tx - sx, dy = ty - sy,
              dr = 20 * Math.sqrt(dx * dx + dy * dy);
          return "M" + sx + "," + sy + "A" + dr + "," + dr + " 0 0,1 " + tx + "," + ty;
        })
        .style("stroke-width", function(d) { return d.value * 1; });

    svg.selectAll(".node")
        .data(graph.nodes)
      .enter().append("circle")
        .attr("class", "node")
        .attr("r", function(d) { return Math.sqrt(d.nodes.length * 5); })
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });

    /*svg.append("g")
        .attr("class", "x axis")
        .call(xAxis);*/

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);
  });
}

 

# Bar Chart

## scaleBand is for bar charts
"When creating bar charts scaleBand helps to determine the geometry of the bars, taking into account padding between each bar. The domain is specified as an array of values (one value for each band) and the range as the minimum and maximum extents of the bands (e.g. the total width of the bar chart)." -- https://github.com/d3/d3-scale#time-scales
```js
var bandScale = d3.scaleBand()
    .domain(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
    .range([0, 200]);

bandScale('Mon'); // returns 0
bandScale('Tue'); // returns 40
bandScale('Fri'); // returns 160
```

## About the Enter set
Scenario: "The number of DOM elements are less than the number of data points in the data set. This means that we need to add the missing elements to the DOM. These data points which don’t have a corresponding DOM element yet and are ready to enter the DOM in the form of DOM visual elements form the Enter set." -- http://rajapradhan.com/blogs/d3-js-v4-essentials/the-enter-update-exit-pattern/

## Set scale functions and ranges
```js
var x = d3.scaleBand().rangeRound([0, width]).padding(0.1);
var y = d3.scaleLinear().rangeRound([height, 0]);
```

## Format data row-by-row
```js
function(d) {
    d.population = +d.population;
    return d;
}
```

## Set domain for x and y
The domain (input) for the x axis is the state abbreviations
```js
x.domain(data.map(function(d) { return d.state; }));
y.domain([0, d3.max(data, function(d) { return d.population; })]);
```

## Add x axis to chart
Move it from the top of the graph to the bottom where it belongs
```js
g.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));
```

## Add y axis to chart
Suggest that D3 use 15 ticks
```js
g.append("g")
    .call(d3.axisLeft(y).ticks(15));
```

## Add bars to the chart
The enter() set is all data that doesn't have an associated DOM element.
The bandwidth() function computes the width of a bar.
The height attribute is measured from the top of the y axis.
```js
g.selectAll(".bar")
  .data(data) 
  .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) { return x(d.state); })
    .attr("y", function(d) { return y(d.population); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(d.population); });
```

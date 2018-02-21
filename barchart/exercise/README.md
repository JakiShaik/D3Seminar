# Bar Chart

## timeParse()
Formats dates or times that you pass it.
```js
var parseTime = d3.timeParse("%B %d, %Y");
parseTime("June 30, 2015"); // Tue Jun 30 2015 00:00:00 GMT-0700 (PDT)
```

## scaleTime == scaleLinear -- kinda
"Time scales are a variant of [linear scales](https://github.com/d3/d3-scale#linear-scales) that have a temporal domain: domain values are coerced to dates rather than numbers, and invert likewise returns a date. Time scales implement ticks based on calendar intervals, taking the pain out of generating axes for temporal domains." -- https://github.com/d3/d3-scale#time-scales
```js
var x = d3.scaleTime()
    .domain([new Date(2000, 0, 1), new Date(2000, 0, 2)])
    .range([0, 960]);

x(new Date(2000, 0, 1,  5)); // 200
x(new Date(2000, 0, 1, 16)); // 640
x.invert(200); // Sat Jan 01 2000 05:00:00 GMT-0800 (PST)
x.invert(640); // Sat Jan 01 2000 16:00:00 GMT-0800 (PST)
```

### Set time parser and scale the axes
```js
var parseDate = d3.timeParse("%Y");
var x = d3.scaleTime().rangeRound([0, width]);
var y = d3.scaleLinear().rangeRound([height, 0]);
```

## Define line
```js
var line = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.percent); });
```

## Format data
```js
function(d) {
    d.year = parseDate(d.year);
    d.percent = +d.percent;
    return d;
}
```

## Scale the data using extent()
```js
x.domain(d3.extent(data, function(d) { return d.year; }));
y.domain([0, d3.max(data, function(d) { return d.percent; })]);
```

## Add x axis to graph
Move it from the top of the graph to the bottom where it belongs
```js
g.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));
```

## Add y axis to graph
Suggest that D3 use 10 ticks
Put a percent sign after each tick label
```js
g.append("g")
    .call(d3.axisLeft(y).ticks(10, "%"));
```

## Add line to graph
```js
g.append("path")
    .datum(data)
    .attr("id", "line")
    .attr("d", line);
```

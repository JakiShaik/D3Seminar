# Scatterplot

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

### Set time parser and scale the axes:
```js
var parseTime = d3.timeParse("%d-%b-%y");
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);
```

## Build line
```js
var valueline = d3.line()
    .x(function (d) {
        return x(d.date);
    })
    .y(function (d) {
        return y(d.close);
    });
```

## Format data
We get to use the time parser we set up earlier now!
```js
data.forEach(function (d) {
    d.date = parseTime(d.date);
    d.close = +d.close;
});
```

## Scale the data using extent()
```js
x.domain(d3.extent(data, function (d) {
    return d.date;
}));
y.domain([0, d3.max(data, function (d) {
    return d.close;
})]);
```

## Add line to plot
```js
svg.append("path")
    .data([data])
    .attr("class", "line")
    .attr("d", valueline);
```

## Put the "Scatter" in "Scatterplot"
```js
svg.selectAll("dot")
    .data(data)
    .enter().append("circle")
    .attr("r", 5)
    .attr("cx", function (d) {
        return x(d.date);
    })
    .attr("cy", function (d) {
        return y(d.close);
    });
```

## Never forget your axes
```js
svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));
svg.append("g")
    .call(d3.axisLeft(y));
```

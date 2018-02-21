# Heat Map Exercise

### Using domain() to define colors:
```js 
const colorScale = d3.scaleQuantile()
    .domain([0, buckets - 1, d3.max(data, (d) => d.value)])
    .range(colors);
```

### Defining data for each card:
```js
const cards = svg.selectAll(".hour")
    .data(data, (d) => d.day+':'+d.hour);
```

### Defining sizes:
```js
cards.enter().append("rect")
    .attr("x", (d) => (d.hour - 1) * gridSize)
    .attr("y", (d) => (d.day - 1) * gridSize)
    .attr("rx", 4)
    .attr("ry", 4)
    .attr("class", "hour bordered")
    .attr("width", gridSize)
    .attr("height", gridSize)
    .style("fill", colors[0])
```

### Transitions:
```js
.merge(cards)
    .transition()
    .duration(1000)
    .style("fill", (d) => colorScale(d.value));
```
### Moar sizes!
```js
legend_g.append("rect")
    .attr("x", (d, i) => legendElementWidth * i)
    .attr("y", height)
    .attr("width", legendElementWidth)
    .attr("height", gridSize / 2)
    .style("fill", (d, i) => colors[i]);
```
### Adding text:
```js
legend_g.append("text")
    .attr("class", "mono")
    .text((d) => "≥ " + Math.round(d))
    .attr("x", (d, i) => legendElementWidth * i)
    .attr("y", height + gridSize);
```

### Event Handlers:
```js
const datasetpicker = d3.select("#dataset-picker")
    .selectAll(".dataset-button")
    .data(datasets);

    datasetpicker.enter()
    .append("input")
    .attr("value", (d) => "Dataset " + d)
    .attr("type", "button")
    .attr("class", "dataset-button")
    .on("click", (d) => heatmapChart(d));
```

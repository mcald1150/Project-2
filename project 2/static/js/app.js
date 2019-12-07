/* data route */

var url = "/data";

function buildPlot() {
  d3.json(url).then(function(response) {

    console.log(response);
    var trace = {
      type: "scatter",
      mode: "lines",
      name: "NYC Shootings",
      x: response.map(data => data.year),
      y: response.map(data => data.sightings),
      line: {
        color: "#17BECF"
      }
    };

    var data = [trace];

    var layout = {
      title: "NYC Shootings Per Year",
      xaxis: {
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();


// console.log("hi40")

// // Select the button
// var button = d3.select("#filter-btn");
// console.log(button);


// button.on("click", function() {
//   // Select the input element and get the raw HTML node
//   var inputElement = d3.select("#datetime");

//   // Get the value property of the input element
//   var inputValue = inputElement.property("value");

//   console.log(inputValue);
//   console.log("hello")


// });


// from data.js
var tableData = data;
// YOUR CODE HERE!
var tbody = d3.select("tbody");

tableData.forEach((d) => {
    var row = tbody.append("tr");
    Object.entries(d).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
});

var button = d3.select("#filter-btn");
button.on("click", runEnter);
  
function runEnter() {
    var inputElement = d3.select("#datetime");

    var inputValue = inputElement.property("value");

    console.log(inputValue);

    var filtered = tableData.filter(data => data.datetime == inputValue);

    console.log(filtered);

    var tbody = d3.select("#ufo-table").select("tbody");
    tbody.html("");

    filtered.forEach((data) => {
        var row = tbody.append("tr");
        Object.entries(data).forEach(([key, value]) => {
          var cell = row.append("td");
          cell.text(value);
    
        });
    });
};
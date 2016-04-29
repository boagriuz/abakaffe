google.charts.load("current", {packages:['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	var stdColor = "blue";
	
	//number of brews per day
	var monBrew = 1;
	var tueBrew = 10;
	var wedBrew = 11;
	var thuBrew = 15;
	var friBrew = 5;
	var satBrew = 30;
	var sunBrew = 1;
	
    var data = google.visualization.arrayToDataTable([
		["Day", "Brews", { role: "style" } ],
        ["Monday", monBrew, stdColor],
        ["Tuesday", thuBrew, stdColor],
        ["Wednesday", wedBrew, stdColor],
        ["Thursday", thuBrew, stdColor],
		["Friday", friBrew, stdColor],
		["Saturday", satBrew, stdColor],
		["Sunday", sunBrew, stdColor]
    ]);

    var view = new google.visualization.DataView(data);
    view.setColumns([0, 1,
                     { calc: "stringify",
                        sourceColumn: 1,
                        type: "string",
                        role: "annotation" },
                    2]);

    var options = {
      title: "Number of brews per week",
      width: 1000,
      height: 400,
      bar: {groupWidth: "95%"},
      legend: { position: "none" },
    };
    var chart = new google.visualization.ColumnChart(document.getElementById("chart_div"));
	  
    chart.draw(view, options);
}
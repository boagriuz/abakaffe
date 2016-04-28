google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {
	  
	var data = new google.visualization.DataTable();
	data.addColumn('string', 'X');
	data.addColumn('number', 'Brews');
	//local variables representing 
	var mondayBrews = 4;
	var tuesdayBrews = 6;
	var wednesdayBrews = 2;
	var thuesdyBrews = 14;
	var fridayBrews = 4;
	var saturdayBrews = 12;
	var sundayBrews = 1;

	data.addRows([
		['mandag', mondayBrews], ['tirsdag', tuesdayBrews], ['onsdag', wednesdayBrews],
		['torsdag', thuesdyBrews], ['fredag', fridayBrews], ['lørdag', saturdayBrews], ['søndag', sundayBrews]
	]);

	var options = {
		hAxis: {
		title: 'Time'
		},
		vAxis: {
		title: 'Brews'
		}
	};

	var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

	chart.draw(data, options);
}
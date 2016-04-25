google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'X');
      data.addColumn('number', 'Brews');

      data.addRows([
        ['mandag', 0],   ['tirsdag', 10],  ['onsdag', 23],  ['torsdag', 17],  ['fredag', 18],  ['lørdag', 9], ['søndag', 3]
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
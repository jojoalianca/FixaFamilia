
  var $ChartStatusImplementasaunPrograma  = $('#ChartStatusImplementasaunPrograma');

  var $ChartStockRan  = $('#ChartStockRan');
  $.ajax({
      url: $ChartStockRan.data("url"),
      success: function (data) {
        var ctx = $ChartStockRan[0].getContext("2d");

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: "Total Pakote",
                    backgroundColor: [
                        'rgba(51, 179, 90, 0.6)',
                        'rgba(151, 79, 0, 0.6)',
                        'rgba(130, 17, 90, 0.6)',
                        'rgba(1, 19, 190, 0.6)',
                        'rgba(151, 479, 192, 0.6)',
                        'rgba(80, 19, 250, 0.6)',
                        'rgba(100, 279, 90, 0.6)'
                    ],
                    borderColor: [
                        'rgba(0, 0, 255, 1)',
                        'rgba(0, 0, 255, 1)',
                        'rgba(0, 0, 255, 1)',
                        'rgba(0, 0, 255, 1)',
                        'rgba(0, 0, 255, 1)',
                        'rgba(0, 0, 255, 1)'
                    ],
                    borderWidth: 1,
                    data: data.data,
                }
            ]
        },
            options : {
              legend: {
                  display: false
              },
              scales: {
                yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      steps: 10,
                      stepValue: 5,
                      precision: 0
                  },
                  scaleLabel: {
                    display: true,
                    labelString: 'Total Pakote',
                  }
                }],
                xAxes: [{
                    scaleLabel: {
                      display: true,
                      labelString: "Grupu RAN",
                    },
                  }]
              }
            }//end of options
    });
    }
    });

  ////////////////////////////////////

  $.ajax({
      url: $ChartStatusImplementasaunPrograma.data("url"),
      success: function (data) {
        var ajaxdata = []
        for (let i in data.programLabels) {
            var totData = []
            for (let j in data.data) {
                totData.push(data.data[j][i])
            }
            ajaxdata.push(totData)
            console.log(ajaxdata)
        }
        var backgroundColor = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462']
        var plotdata = []
        for (let i in ajaxdata) {
            plotdata.push({
                label: data.programLabels[i],
                data: ajaxdata[i],
                backgroundColor: backgroundColor[i],
                borderColor: backgroundColor[i],
                borderWidth: 1
            },)
        }
        var ctx = $ChartStatusImplementasaunPrograma[0].getContext("2d");

        new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: plotdata
        },
            options : {
              legend: {
                  display: true
              },
              scales: {
                yAxes: [{
                  ticks: {
                      beginAtZero: true,
                      steps: 10,
                      stepValue: 5,
                      precision: 0
                  },
                  scaleLabel: {
                    display: true,
                    labelString: 'Total Implementasaun',
                  }
                }],
                xAxes: [{
                    scaleLabel: {
                      display: true,
                      labelString: "Status Implementasaun",
                    },
                  }]
              }
            }//end of options
    });
    }
    });

  ////////////////////////////////////

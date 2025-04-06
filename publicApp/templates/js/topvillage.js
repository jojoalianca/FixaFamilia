document.addEventListener("DOMContentLoaded", () => {
  // Get the container element
  const chartElement = document.querySelector("#topV");
  
  // Only proceed if the element exists
  if (!chartElement) return;

  // Prepare data from Django template variables
  const sukuNames = [];
  const sukuPopulations = [];

  {% for suku in top_sukus %}
    sukuNames.push("{{ suku.name|escapejs }}");
    sukuPopulations.push({{ suku.total }});
  {% endfor %}

  // Create chart only if we have data
  if (sukuNames.length > 0 && sukuPopulations.length > 0) {
    new ApexCharts(chartElement, {
      series: [{
        name: 'Total Populasaun',
        data: sukuPopulations
      }],
      chart: {
        height: 400,
        type: 'bar',
        toolbar: {
          show: false
        },
      },
      plotOptions: {
        bar: {
          borderRadius: 4,
          horizontal: true,
          distributed: true
        }
      },
      colors: ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'],
      dataLabels: {
        enabled: true,
        formatter: function(val) {
          return val.toLocaleString(); // Format numbers with commas
        },
        style: {
          fontSize: '12px',
          colors: ["#000000"]
        }
      },
      xaxis: {
        categories: sukuNames,
        title: {
          text: 'Total Populasaun',
          style: {
            fontSize: '14px',
            fontWeight: 'bold'
          }
        },
        labels: {
          style: {
            fontSize: '12px'
          }
        }
      },
      yaxis: {
        title: {
          text: 'Naran Suku',
          style: {
            fontSize: '14px',
            fontWeight: 'bold'
          }
        },
        labels: {
          style: {
            fontSize: '12px'
          }
        }
      },
      tooltip: {
        y: {
          formatter: function(value) {
            return value.toLocaleString() + " ema"; // Example: "1,234 ema"
          }
        }
      },
      responsive: [{
        breakpoint: 768,
        options: {
          chart: {
            height: 300
          },
          dataLabels: {
            enabled: false
          }
        }
      }]
    }).render();
  } else {
    // Show message if no data
    chartElement.innerHTML = '<div class="alert alert-info">Dadus la iha</div>';
  }
});
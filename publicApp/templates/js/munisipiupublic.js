document.addEventListener("DOMContentLoaded", () => {
  new ApexCharts(document.querySelector("#publicmunisipiu"), {
    series: [{
      name: 'Total',
      data: ["{% for xx in loopingestudantesexo %}","{{xx.total_estudantes|floatformat:'3'}}","{% endfor %}"]
    }],
    chart: {
      height: 400,
      type: 'bar',
      toolbar: {
        show: false
      },
    },
    markers: {
      size: 12
    },
    colors: ['#a3e4d7', '#B3B6B7','#4E342E',],
    fill: {
      type: "gradient",
      gradient: {
        shadeIntensity: 1,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 90, 100]
      }
    },
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: 'smooth',
      width: 1
    },
    xaxis: {
      type: 'text',
      categories: ["{% for ii in loopingestudantesexo %}","{{ii.name}}","{% endfor %}"]
    },
    tooltip: {
      x: {
        format: 'dd/MM/yy HH:mm'
      },
    }
  }).render();
});

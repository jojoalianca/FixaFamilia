// Data untuk Aldeia
    var aldeiaLabels = [{% for a in aldeia_stats %}"{{ a.name }}",{% endfor %}];
    var aldeiaMane = [{% for a in aldeia_stats %}{{ a.total_mane }},{% endfor %}];
    var aldeiaFeto = [{% for a in aldeia_stats %}{{ a.total_feto }},{% endfor %}];
    var aldeiaTotal = [{% for a in aldeia_stats %}{{ a.total_warga }},{% endfor %}];

    var ctxAldeia = document.getElementById('aldeiaChart').getContext('2d');
    new Chart(ctxAldeia, {
        type: 'bar',
        data: {
            labels: aldeiaLabels,
            datasets: [
                {
                    label: 'Mane',
                    data: aldeiaMane,
                    backgroundColor: 'blue'
                },
                {
                    label: 'Feto',
                    data: aldeiaFeto,
                    backgroundColor: 'pink'
                },
                {
                    label: 'Total Cidadaun (Inklui Chefe Familia)',
                    data: aldeiaTotal,
                    backgroundColor: 'gray'
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
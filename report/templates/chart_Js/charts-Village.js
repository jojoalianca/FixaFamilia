 // Data untuk Village
    var villageLabels = [{% for v in village_stats %}"{{ v.name }}",{% endfor %}];
    var villageMane = [{% for v in village_stats %}{{ v.total_mane }},{% endfor %}];
    var villageFeto = [{% for v in village_stats %}{{ v.total_feto }},{% endfor %}];
    var villageTotal = [{% for v in village_stats %}{{ v.total_warga }},{% endfor %}];

    var ctxVillage = document.getElementById('villageChart').getContext('2d');
    new Chart(ctxVillage, {
        type: 'bar',
        data: {
            labels: villageLabels,
            datasets: [
                {
                    label: 'Mane',
                    data: villageMane,
                    backgroundColor: 'red'
                },
                {
                    label: 'Feto',
                    data: villageFeto,
                    backgroundColor: 'pink'
                },
                {
                    label: 'Total Cidadaun (Inklui Chefe Familia)',
                    data: villageTotal,
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

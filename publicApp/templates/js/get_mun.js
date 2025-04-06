document.getElementById('searchInput').addEventListener('input', function() {
    var searchTerm = this.value;

    // Fetch the data based on the search term
    fetch(`/get_municipios/?search=${searchTerm}`)
        .then(response => response.json())
        .then(data => {
            // Clear the existing list items
            const listContainer = document.getElementById('municipioList');
            listContainer.innerHTML = '';

            // Check if there is data
            if (data.length === 0) {
                listContainer.innerHTML = '<li class="list-group-item">No municipalities found.</li>';
            }

            // Add each municipality to the list
            data.forEach(municipio => {
                const listItem = document.createElement('li');
                listItem.classList.add('list-group-item');

                listItem.innerHTML = `
                    <b>${municipio.name}</b>
                    <span class="badge badge-primary float-right">
                        Total Klinik: ${municipio.total_klinik}
                    </span>
                `;

                listContainer.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});

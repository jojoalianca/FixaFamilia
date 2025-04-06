document.addEventListener("DOMContentLoaded", function () {
    // Inisialisasi peta
    var map = L.map('map', {
        fullscreenControl: true, // Tambahkan kontrol fullscreen
    }).setView([-8.5593, 125.5795], 9);

    // Layer peta jalan (OpenStreetMap)
    var streetLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Layer peta satelit (Mapbox Satellite)
    var satelliteLayer = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=YOUR_MAPBOX_ACCESS_TOKEN', {
        attribution: '&copy; <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18
    });

    // Kontrol untuk mengganti layer peta
    var baseLayers = {
        "Street Map": streetLayer,
        "Satellite Map": satelliteLayer
    };
    L.control.layers(baseLayers).addTo(map);

    // Fungsi untuk mengganti tampilan peta
    function toggleMapView() {
        if (map.hasLayer(streetLayer)) {
            map.removeLayer(streetLayer);
            map.addLayer(satelliteLayer);
        } else {
            map.removeLayer(satelliteLayer);
            map.addLayer(streetLayer);
        } 
    }
    window.toggleMapView = toggleMapView;

    // Warna berdasarkan tipe klinik
    function getColor(tipo) {
        return tipo === 'Privadu' ? '#007bff' : '#dc3545'; // Biru untuk Privadu, Merah untuk Publiku
    }

    // Ambil data klinik dari tabel ClienteRaiPoint dan tampilkan di peta
    fetch("{% url 'klinik_map_data' %}")  
        .then(response => response.json())
        .then(data => {
            data.clinics.forEach(clinic => {
                if (clinic.latitude && clinic.longitude) {
                    var marker = L.circleMarker([clinic.latitude, clinic.longitude], {
                        radius: 8,
                        fillColor: getColor(clinic.type),
                        color: "#000",
                        weight: 1,
                        opacity: 1,
                        fillOpacity: 0.8
                    }).addTo(map);

                    // Format Popup untuk klinik
                    var popupContent = `
                        <div class="popup-content">
                            <h4>${clinic.name}</h4>
                            ${clinic.image_url ? `<img src="${clinic.image_url}" alt="Image" class="popup-image">` : ''}
                            <p><b>Responsável:</b> ${clinic.responsavel || "N/A"}</p>
                            <p><b>Município:</b> ${clinic.municipality}</p>
                        </div>
                    `;
                    marker.bindPopup(popupContent, {
                        className: 'custom-popup' // Tambahkan class untuk styling popup
                    });
                }
            });
        });

    // Ambil data statistik klinik dan tampilkan dalam peta sebagai card
    fetch("{% url 'klinik_summary' %}")
        .then(response => response.json())
        .then(data => {
            // Koordinat titik pusat untuk setiap município
            var municipioCenters = {
                "Dili": [-8.549521326383436, 125.55810394314027],
                "Baucau": [-8.471, 126.457],
                "Ermera": [-8.7514, 125.3944]
            };

            // Iterasi melalui setiap município dan gambarkan titik untuk representasi klinik
            Object.keys(municipioCenters).forEach(municipality => {
                var totalPrivadu = data.summary[municipality].Privadu || 0;
                var totalPubliku = data.summary[municipality].Publiku || 0;

                var coords = municipioCenters[municipality];

                // Tambahkan marker (titik) untuk setiap município
                if (coords) {
                    var marker = L.marker(coords, {
                        icon: L.icon({
                            iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
                            iconSize: [25, 41],
                            iconAnchor: [12, 41]
                        })
                    }).addTo(map);

                    // HTML untuk Card yang menampilkan informasi klinik
                    var cardContent = `
                        <div class="clinic-card">
                            <h4>${municipality}</h4>
                            <p><b>Total Klinik Privadu:</b> ${totalPrivadu}</p>
                            <p><b>Total Klinik Publiku:</b> ${totalPubliku}</p>
                            <button class="close-card">Close</button>
                        </div>
                    `;

                    // Tambahkan popup pada marker
                    marker.bindPopup(cardContent, {
                        className: 'custom-popup', // Styling untuk popup card
                        closeButton: false // Menonaktifkan tombol close default
                    });

                    // Event listener untuk menutup card popup
                    marker.on('popupopen', function() {
                        var closeButton = marker._popup.getElement().querySelector('.close-card');
                        closeButton.addEventListener('click', function() {
                            marker.closePopup(); // Menutup popup ketika tombol "Close" diklik
                        });
                    });
                }
            });
        });

    // Fitur pencarian município
    document.getElementById('searchInput').addEventListener('input', function() {
        var searchTerm = this.value;

        fetch(`/get_municipios/?search=${searchTerm}`)
            .then(response => response.json())
            .then(data => {
                // Update the list or map based on the received data
                console.log(data);  // Data contains the name and total_klinik for each municipality
            });
    });
});
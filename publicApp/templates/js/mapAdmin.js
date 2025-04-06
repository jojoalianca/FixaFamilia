{% load static %}
// Inisialisasi peta
var map = L.map('map', {
    fullscreenControl: true, // Tambahkan kontrol full screen
}).setView([-8.5569, 125.5603], 8); // Default Timor-Leste

// Tambahkan peta dasar dari OpenStreetMap
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
});

// Tambahkan layer satelit dari Mapbox
var satelliteLayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: '© Mapbox',
    id: 'mapbox/satellite-v9',
    accessToken: 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', // Ganti dengan token Mapbox Anda
    tileSize: 512,
    zoomOffset: -1
});

// Tambahkan layer default (satelit)
satelliteLayer.addTo(map);

// Tambahkan kontrol layer untuk beralih antara peta dasar dan satelit
var baseMaps = {
    "Peta Dasar": baseLayer,
    "Satelit": satelliteLayer
};
L.control.layers(baseMaps).addTo(map);

// Buat ikon kustom untuk tipe klinik
var redIcon = L.icon({
    iconUrl: '{% static "icons/blue-icon.png" %}', // Ikon merah untuk Privadu
    iconSize: [38, 38],
    iconAnchor: [19, 38],
    popupAnchor: [0, -38]
});

var greenIcon = L.icon({
    iconUrl: '{% static "icons/green-icon.png" %}', // Ikon hijau untuk Public
    iconSize: [38, 38],
    iconAnchor: [19, 38],
    popupAnchor: [0, -38]
});

// Data lokasi dari template Django
var locations = [
    {% for point in cordinate %}
        {% if point.latitude and point.longitude %}
            {
                lat: {{ point.latitude }},
                lng: {{ point.longitude }},
                name: "{{ point.klinika.naran_klinik }}",
                tipo: "{{ point.klinika.tipo_klinik }}",
                image: "{% if point.image %}{{ point.image.url }}{% endif %}"
            },
        {% endif %}
    {% endfor %}
];

// Tambahkan marker untuk setiap lokasi
locations.forEach(function(loc) {
    var icon = loc.tipo === 'Privadu' ? redIcon : greenIcon; // Pilih ikon berdasarkan tipe klinik
    var popupContent = `
        <div class="popup-content">
            <h6>${loc.name}</h6>
            <p><strong>Tipo Klinik:</strong> ${loc.tipo}</p>
            <p><strong>Lat:</strong> ${loc.lat}, <strong>Lng:</strong> ${loc.lng}</p>
            ${loc.image ? `<img src="${loc.image}" alt="Lokasi Gambar" class="img-thumbnail" style="max-width: 100%;">` : ''}
        </div>
    `;
    var marker = L.marker([loc.lat, loc.lng], { icon: icon }).addTo(map);
    marker.bindPopup(popupContent);  // Popup akan muncul saat marker diklik
});

// Atur tampilan peta ke lokasi pertama jika ada
if (locations.length > 0) {
    map.setView([locations[0].lat, locations[0].lng], 14);
}
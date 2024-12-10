const map = L.map('map_here', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


const airportMarkers = L.featureGroup().addTo(map);


const marker = L.marker([60.688477, 24.472502]).addTo(map);
//latitude longitude
airportMarkers.addLayer(marker);

console.log("end")
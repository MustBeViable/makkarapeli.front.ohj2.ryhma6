
async function map_js_juttu () {const map = L.map('map_here', {tap: false});
  L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
  }).addTo(map);
  map.setView([60, 24], 1);


  const airportMarkers = L.featureGroup().addTo(map);



//const marker = L.marker([60.688477, 24.472502]).addTo(map);
//latitude longitude

  console.log('end');
  return [airportMarkers, map]
}
/**
 *     <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
 *     <script src="https://unpkg.com/leaflet/dist/leaflet.js" defer></script>
 *     <script src="/Game/Javascript/map.js" defer></script>
 */
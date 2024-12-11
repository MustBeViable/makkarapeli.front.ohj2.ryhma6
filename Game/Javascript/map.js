
const map = L.map('map_here', {tap: false});
  L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
  }).addTo(map);

  map.setView([60, 24], 2);


  const airportMarkers = L.featureGroup().addTo(map);



//const marker = L.marker([60.688477, 24.472502]).addTo(map);
//latitude longitude

  console.log('end');
/**
  const mymakkaraicon = L.Icon({
    iconUrl:'../images_and_other/logo.png',

    iconSize:     [38, 95], // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor

  })
**/
/**
 *     <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>
 *     <script src="https://unpkg.com/leaflet/dist/leaflet.js" defer></script>
 *     <script src="/Game/Javascript/map.js" defer></script>
 */
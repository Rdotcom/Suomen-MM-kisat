document.addEventListener('DOMContentLoaded', function() {
  const map = L.map('map').setView([33.755489, -84.401993], 3);
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
  }).addTo(map);

  const locations = [
    {name: 'Rogers Centre, Kanada', lat: 43.641796, lng: -79.390083},
    {name: 'BC Place Vancouver, Kanada', lat: 49.272665576, lng: -123.107166238,},
    {name: 'Estadio Azteca, Meksiko', lat: 19.3017454597, lng: -99.1502643989},
    {name: 'Estadio Jalisco, Meksiko', lat: 20.703002188, lng: -103.323553706},
    {name: 'Estadio de Béisbol Monterrey, Meksiko', lat: 25.7177737956, lng: -100.309448762,},
    {name: 'Mercedes-Benz Stadium, USA', lat: 33.755489, lng: -84.401993},
    {name: 'Fenway Park, USA', lat: 42.346268, lng: -71.095764},
    {name: 'AT&T Stadium, USA', lat: 32.747841, lng: -97.093628},
    {name: 'NRG Stadium, USA', lat: 29.68416393, lng: -95.406498374},
    {name: 'Arrowhead Stadium, USA', lat: 39.042666496, lng: -94.483664732},
    {name: 'SoFi Stadium, USA', lat: 33.953587, lng: -118.339630},
    {name: 'Hard Rock Stadium, USA', lat: 25.957960, lng: -80.239311},
    {name: 'MetLife Stadium, USA', lat: 40.813778, lng: -74.074310},
    {name: 'Lincoln Financial Field, USA', lat: 39.900898, lng: -75.168098},
    {name: 'Levis Stadium, USA', lat: 37.4020148919, lng: -121.968869091},
    {name: 'CenturyLink Field, USA', lat: 47.590497638, lng: -122.325665364},
  ];

  locations.forEach(function(location) {
    let marker = L.marker([location.lat, location.lng], { doubleClicked: false }).addTo(map);

    marker.on('dblclick', function() {
      if (!marker.doubleClicked) {
        window.location.href = 'penalties.html';
        marker.doubleClicked = true;

        // Vaihdetaan markeri punaiseksi
        marker.setIcon(blockedMarkerIcon);
      }
    });

    marker.bindPopup(location.name);
  });
});

const blockedMarkerIcon = L.icon({
  iconUrl: 'img/redmarker.png',
  iconSize: [20, 32],
  iconAnchor: [16, 32],
  popupAnchor: [0, -32]
});

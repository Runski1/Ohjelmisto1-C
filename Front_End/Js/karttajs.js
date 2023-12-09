'use strict';
import { cityData } from "./cities.js";
// We'll use import functionality to get citydata from another file
// Don't forget to replace <YOUR_ACCESS_TOKEN> by your real access token!
const accessToken = 'c6moPjpSN7QLOooqQRQkhGSswG714yj1foLNEIYWMqAcvVJVqx1LFPDqpl9tCvet';
// We can set view to player coords aswell
const map = L.map('map').setView([53.551086, 9.993682], 4);
L.tileLayer(
  `https://tile.jawg.io/jawg-dark/{z}/{x}/{y}.png?access-token=${accessToken}`, {
    attribution: '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank" class="jawg-attrib">&copy; <b>Jawg</b>Maps</a> | <a href="https://www.openstreetmap.org/copyright" title="OpenStreetMap is open data licensed under ODbL" target="_blank" class="osm-attrib">&copy; OSM contributors</a>',
    maxZoom: 22
  }
).addTo(map);

// Adding different markers
let greenMarker = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
	iconSize: [12, 20],
	iconAnchor: [12, 20],
	popupAnchor: [-5, -15],
	shadowSize: [20, 20]
});
let greyMarker = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-grey.png',
	shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
	iconSize: [12, 20],
	iconAnchor: [12, 20],
	popupAnchor: [-5, -15],
	shadowSize: [20, 20]
});
let redMarker = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
	shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
	iconSize: [12, 20],
	iconAnchor: [12, 20],
	popupAnchor: [-5, -15],
	shadowSize: [20, 20]
});

// Here we should render all map markers
console.log(cityData)
for (let city of cityData){
  let marker = L.marker([city.latitude_deg, city.longitude_deg], {icon: greyMarker}).addTo(map);
  marker.bindPopup(city.name)
}
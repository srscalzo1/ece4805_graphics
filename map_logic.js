// map_script.js

var myMap;

function setMap(){
    myMap = L.map('map').setView([40.7128, -74.0060], 11);  // Set initial coordinates and zoom level
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(myMap);
}

function updateMap(lat, lon) {
    if (myMap) {
        myMap.setView([lat, lon], 11);  // Dynamically update map view
        L.marker([lat, lon]).addTo(myMap).bindPopup("Home Location");
    }
}

function selectCoordinates(lat, lon) {
    //updateMap(lat, lon);
    alert("Coordinates selected: " + lat + ", " + lon);  // Optional: Alert to show the selected coordinates
}

function goHome() {
    updateMap(40.7128, -74.0060);  // Example: Go to a predefined home location (New York)
    alert("Going home!");
}
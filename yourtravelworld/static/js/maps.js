function mapInit() {
  var cords = { lat: -34.86, lng: 138.51 };
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: cords,
    scrollwheel:  false,
  });

  // This event listener calls addMarker() when the map is clicked.
  google.maps.event.addListener(map, 'click', function(event) {
    addMarker(event.latLng, map);
  });

  // Add a marker at the center of the map.
  addMarker(cords, map);

  // Adds a marker to the map.
  function addMarker(location, map) {
    // Add the marker at the clicked location, and add the next-available label
    // from the array of alphabetical characters.
    var marker = new google.maps.Marker({
      position: location,
      //- label: labels[labelIndex++ % labels.length],
      map: map
    });
  }
}

google.maps.event.addDomListener(window, 'load', mapInit);

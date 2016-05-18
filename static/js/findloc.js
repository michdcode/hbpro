<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places"></script>

service = new google.maps.places.PlacesService(map);

service.textSearch(request, callback);
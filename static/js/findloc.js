

var service;

function initialize() {
    var request = {
        query: 'Paris'
    };

service = new google.maps.places.PlacesService();
service.textSearch(request, callback);
}

function callback(results, status) {
    if(status == google.maps.places.PlacesServiceStatus.OK) {
        for(var i=0; i < results.length; i++) {
            var place = results[i];
        }
    }
        trace(results);
}

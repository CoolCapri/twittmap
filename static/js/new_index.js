$( document ).ready(function() {
    $('#searchbuttonid').on('click', searchKeyword);
});

var ourMap;
var markerClusterer = null;
var coordinates_lat = [];
var coordinates_lng = [];
var created_at = [];
var tweets = [];
var markers = [];

function searchKeyword(){
  var keyword = $('#serachbox').val();
  httpGetAsync("searchf/", keyword);
}

function searchKeyword2(keyword){
  httpGetAsync("searchf/", keyword);
}

function initMap() {
	var myLatLng = {
		lat: 39.8282,
		lng: -98.5795
	};

  var myLatLng2 = {
    lat: 50.0,
    lng: -100.0
  };

	ourMap = new google.maps.Map(document.getElementById('map'), {
		zoom: 3,
		center: myLatLng,
    zoomControl: true,
    zoomControlOptions: {
      position: google.maps.ControlPosition.RIGHT_CENTER
    }
	});
}

function resetVariables(){
  coordinates_lat = [];
  coordinates_lng = [];
  created_at = [];
  tweets = [];
  deleteMarkers();
}
//handle the search part
function httpGetAsync(theUrl, keyword) {
  resetVariables()
  $.getJSON(theUrl, function(result){
      processJsonResult(result, keyword);
  });
}

function processJsonResult(result, keyword) {
  var tweets_list = result[keyword];
  if (tweets_list == null) {
    alert("No results found");
    return;
  }

  for (var i = 0; i < tweets_list.length; i++) {
      var tweet = tweets_list[i];
      coordinates_lng.push(tweet.coordinates[0]);
      coordinates_lat.push(tweet.coordinates[1]);
      created_at.push(tweet.created_at);
      tweets.push(tweet.text);
  }
  generateMarkers();
}

function generateMarkers() {
  for (var i = 0; i < tweets.length; i++) {
    var location = {
      lat: parseFloat(coordinates_lat[i]),
      lng: parseFloat(coordinates_lng[i])
    };

    var marker = new google.maps.Marker({
  		position: location,
  		title: 'Hello World!'
  	});

    markers.push(marker);
    markerClusterer = new MarkerClusterer(ourMap, markers);
  }
}

function myFunction2() {
	document.getElementById("myDropdown2").classList.toggle("show");
}



function filterFunction() {
	var input, filter, ul, li, a, i;
	input = document.getElementById("myInput");
	filter = input.value.toUpperCase();
	div = document.getElementById("myDropdown");
	a = div.getElementsByTagName("a");
	for (i = 0; i < a.length; i++) {
		if (a[i].innerHTML.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "";
		} else {
			a[i].style.display = "none";
		}
	}
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
  setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
  setMapOnAll(ourMap);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  markers = [];
}
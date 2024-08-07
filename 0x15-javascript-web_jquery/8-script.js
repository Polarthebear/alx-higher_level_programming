$(document).ready(function() {
    $.ajax({
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	method: 'GET'
	success: function(data) {
	    var films = data.results;
	    var movieList = '';
	    $.each(films, function(index, film) {
	       movieList += '<li>' + film.title + '</li>';
	    });
	    $('#list_movies').html(movieList);
	},
	error: function() {
	     $('#list_movies').html('<li>Failed to load movie titles.</li>');
	}
    });
});

$(document).ready(function() {
	$.ajax({
	   url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
	   method: 'GET',
	   success: function(data) {
		var helloTranslation = data.hello;
		$('#hello').text(helloTranslation);
	   },
	   error: function() {
		$('#hello').text('Failed to load translation.');
	   }
	});
});

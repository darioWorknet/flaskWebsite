$(document).ready(function() {

	$('.image_overlay h5').html('VIEW PROJECTS');
	$('#header .image_overlay h5').html('CV');
	$('.second h5').html('VIEW MORE');
	
	breakpoints({
		large:   [ '801px',   '1800px'  ],
		small:  [ null,      '800px'  ],
	});

	breakpoints.on('>small', function() {
		$('#footer').appendTo($('#header'));
		$('#footer').addClass('header_content');
		$('.icons').addClass('move_to_left');
	});

	breakpoints.on('<=small', function() {
		$('#footer').insertAfter($('#main'));
		$('#footer').removeClass($('header_content'));
		$('.icons').removeClass($('move_to_left'));

	});

});



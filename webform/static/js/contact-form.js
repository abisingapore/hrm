$(document).ready(function() {
	$("#submit-btn").click(function() {
		//collection of input values//
		var user =  $('input[name=name]').val();
		var email =  $('input[name=email]').val();
		var message =  $('input[name=message]').val();

		//simple validation
		var proceed = true;
		if(user==""){
			$('input[name=name]').css('.border-color', 'red');
			proceed=false;
		}
		if(email==""){
			$('input[name=email]').css('.border-color', 'red');
			proceed=false;
		}
		if(message==""){
			$('input[name=message]').css('.border-color', 'red');
			proceed=false;
		}

		if(proceed) {
			post_data = {'userName':name, 'userEmail':email, 'userMessage':message  };

			$post('contact.php', post_data, function(data){
				$("#result").hide().html('<div class="success">'+data+'</div>').slideDown();

				$('#contact_form input').val('');
				$('#contact_form textarea').val('');

			}).fail(function(err) {
				$("#result").hide().html('<div class="error">'+err.statusText+'</div>').slideDown();
			});
		}
	});

	$("#contact_form input, #contact_form textarea").keyup(function() {
		$("#contact_form input, #contact_form textarea").css('border-color', '');
		$('#result').slideUp();
	});
});	
$(document).ready(function() {
	
	function get_data(form){
		dataform = new FormData();
		form.find('input, textarea, select').each(function(){ 
			element=$(this);
			dataform.append(element.attr('name'), element.val());
			console.log(element.val())
		});
	    console.log('dataform');
	    console.log(dataform);
		return dataform;
	}
	
	var procesando= function timeout_trigger(){
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init(){
		setTimeout(procesando, 3000);
	}

	$(document).on("click","[class*=boton_reservar_reserva]",function(){
		var form = $(this).parent().parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});
	
	$(document).on("click","[class*=boton-reservar-pista]",function(){
		var div = $(this).parent();
		var form=$(div).find('form');
		console.log(form)
		if ($(form).hasClass('hide')){
			$(form).removeClass('hide');
		}
		else{
			$(form).addClass('hide');
		}
		
	});

	$(document).on("submit","[class*=formulario-reservar-reserva]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			change_element(form);
			event.stopPropagation();
		});
	});

	function change_element(form){
		console.log('change')
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		dataform = get_data(form)
		$.ajax({
			url : $(form).attr('action'), 
			data:$(form).serialize(),
			type: 'POST',
			success : function(response_data) {
				if (response_data.hay_error){
            		var html ='';
            		html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
                    html+='<h2 class="text-danger"><strong>Han ocurrido errores</strong></h2></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
            					html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
            					html+='<strong><p class="text-danger">' + key + ": " + response_data[key] + '</p></strong>';
            					html+='</div></div>';
            				}
              				 console.log(key + " -> " + response_data[key]);
            			}
            		}
            		html+='<br/>';
        		}
        		else{
            		var html ='';
            		html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
                    html+='<h2 class="text-success"><strong>Reserva realizada</strong></h2></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
            					html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
            					html+='<strong><p class="text-success">' + key + ": " + response_data[key] + '</p></strong>';
            					html+='</div></div>';
            				}
              				 console.log(key + " -> " + response_data[key]);
            			}
            		}
            		html+='<br/>';
        		}
				var body = $('my-modal-user').find('.modal-body');
				$('.info_ok').html(html);
				$('#my-modal-user').modal('show');
		    },
		    error : function(xhr,errmsg,err) {
		    	$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
		    	" <a href='#' class='close'>&times;</a></div>"); 
		    	console.log(xhr.status + ": " + xhr.responseText);
		    }
		});
		console.log('fin change')
	};
	
});
$(document).ready(function() {
	
	$(".formulario-crear-usuario").each(function(index) {
	    $(this).on("submit", function(event){
	    	event.preventDefault();
			var form = $(this);
			create_element(form);
	    });
	});
	
	$(".formulario-crear-login").each(function(index) {
	    $(this).on("submit", function(event){
	    	event.preventDefault();
			var form = $(this);
			login(form);
	    });
	});
	
	$(".boton-crear-usuario").each(function(index) {
	    $(this).on("click", function(){
	    	var form = $(this).parent();
			console.log(form);
			event.preventDefault();
			form.submit();
	    });
	});
	
	$(".boton-crear-login").each(function(index) {
	    $(this).on("click", function(){
	    	var form = $(this).parent();
			console.log(form);
			event.preventDefault();
			form.submit();
	    });
	});

	function get_data(form){
		dataform = new FormData();
		console.log(form);
		form.find('input, textarea, select').each(function(){ 
			element=$(this);
			console.log(element);
			console.log(element.val());
			dataform.append(element.attr('name'), element.val());
		});
	    console.log('dataform');
	    console.log(dataform);
		return dataform;
	}
	
	var procesando= function timeout_trigger() {
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init() {
	    setTimeout(procesando,3000);
	}
	
	function create_element(form) {
		event.stopPropagation();
	    event.preventDefault();
		dataform=get_data(form);
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		$.ajax({
			url : form.attr('action'),
			data: dataform,
		    cache: false,
		    contentType: false,
		    processData: false,
		    type: 'POST',
        	success : function(response_data) {
        		if (response_data.hay_error){
            		var html ='';
            		html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
                    html+='<h1 class="text-danger"><strong>Han ocurrido errores</strong></h1></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
              				  	html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
              				  	console.log(key + " -> " + response_data[key]);
            				  	html+='<strong><p class="text-danger">' + key + ": " + response_data[key] + '</p></strong>';
            				  	html+='</div></div>';
              			  	}
            			}
            		}
            		html+='<br/>';
        		}
        		else{
            		var html ='';
            		html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
                    html+='<h1 class="text-success"><strong>Se ha realizado la creacion</strong></h1></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
            					html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
              				  	console.log(key + " -> " + response_data[key]);
              				  	html+='<strong><p class="text-success">' + key + ": " + response_data[key] + '</p></strong>';
              				  	html+='</div></div>';
              			  	}
            			}
            		}
            		html+='<br/>';
        		}
        		$('.image_ajax').addClass('hide');
        		$('.info').append(html);
        		$('#my-modal-user').modal('show');
        	},
        	error : function(xhr,errmsg,err) {
        		$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                	" <a href='#' class='close'>&times;</a></div>"); 
        		console.log(xhr.status + ": " + xhr.responseText);
        	}
		});
	};
	
	function login(form) {
		event.stopPropagation();
	    event.preventDefault();
		var dataform =get_data(form);
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		console.log(form.serialize());
		$.ajax({
			url : form.attr('action'),
			data: dataform,
		    cache: false,
		    contentType: false,
		    processData: false,
		    type: 'POST',
        	success : function(response_data) {
        		if (response_data.hay_error){
            		var html ='';
            		html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
                    html+='<h1 class="text-danger"><strong>Han ocurrido errores</strong></h1></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
              				  	html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
              				  	console.log(key + " -> " + response_data[key]);
            				  	html+='<strong><p class="text-danger">' + key + ": " + response_data[key] + '</p></strong>';
            				  	html+='</div></div>';
              			  	}
            			}
            		}
            		html+='<br/>';
            		$('.image_ajax').addClass('hide');
            		$('.info').append(html);
            		$('#my-modal-user').modal('show');
        		}
        		else{
        			window.location = response_data.url;
        		}
      
        	},
        	error : function(xhr,errmsg,err) {
        		$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                	" <a href='#' class='close'>&times;</a></div>"); 
        		console.log(xhr.status + ": " + xhr.responseText);
        	}
		});
	};

	$('.bxslider').bxSlider({
		  minSlides: 3,
		  maxSlides: 4,
		  slideWidth: 300,
		  slideMargin: 10
		});

});
$(document).ready(function() {

	var procesando= function timeout_trigger(){
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init(){
		setTimeout(procesando, 3000);
	}
	
	$(document).on("submit","[class*=form-consultar-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			var key = form.find('input:hidden[name=pk]').val();
			var tipe = form.find('input:hidden[name=tipe]').val();
			retrieve_element(key, tipe, form);
			event.stopPropagation();
		});
	});
	
	$(document).on("click","[class*=boton-consultar-]",function(){
		var form = $(this).parent();
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});

	function retrieve_element(key, tipe, form) {
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')'); 
		console.log('retrieve')
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
	    event.stopPropagation(); 
	    event.preventDefault(); 
		var clave = key;
		var consultar = form.find('input:hidden[name=consultar]').val();
		$.ajax({
			url : form.attr('action'),
			data : { 
				pk:parseInt(key),
				tipe:tipe,
				consultar:consultar,
			},
		    type: 'POST',
		    success : function(response_data) {
				var html ='';
				for (var key in response_data) {
        			if(key != 'hay_error'){
        				if (response_data.hasOwnProperty(key)) {
        					html+='<div class="row text_centre"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
          				  	if (key=='Imagen'){
          				  		html+='<strong><p class="text-success">';
          				  		html+='<p><img class="consulta img-responsive img-thumbnail" src="/media/' + response_data[key] + '" alt=""></p></strong>';
          				  	}
          				  	else{
          				  		html+='<strong><p class="text-success">' + key + ": " + response_data[key] + '</p></strong>';
          				  	}
          				  	html+='</div></div>';
          			  	}
        			}
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
		console.log('fin retrieve');
	};
	
});
$(document).ready(function() {

	var procesando= function timeout_trigger(){
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init(){
		setTimeout(procesando, 3000);
	}
	
	$(document).on("submit","[class*=form-borrar-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			var key = form.find('input:hidden[name=pk]').val();
			var tipe = form.find('input:hidden[name=tipe]').val();
			delete_element(key, tipe, form);
			event.stopPropagation();
		});
	});
	
	$(document).on("click","[class*=boton-borrar-]",function(){
		var form = $(this).parent();
		event.preventDefault();
		event.stopPropagation();
		if (confirm('¿Desea eliminar el elemento?')) {
			form.submit();
		} else {
		    return false;
		}
	});
	
	function delete_element(key, tipe, form) {
		console.log('retrieve')
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
	    event.stopPropagation(); 
	    event.preventDefault(); 
		var clave = key;
		var borrar = form.find('input:hidden[name=borrar]').val();
		$.ajax({
			url : form.attr('action'), // the endpoint
			data : { 
				pk:parseInt(key),
				tipe:tipe,
				borrar:borrar,
			},
		    type: 'POST',
		    success : function(response_data) {
            		var html ='';
            		html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
                    html+='<h1 class="text-success"><strong>Se ha realizado el borrado</strong></h1></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
            					html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
              				  	html+='<strong><p class="text-success">' + key + ": " + response_data[key] + '</p></strong>';
              				  	html+='</div></div>';
              			  	}
            			}
            		}
            	html+='<br/>';
				var body = $('my-modal-user').find('.modal-body');
				$('.info_ok').html(html);
				$('#my-modal-user').modal('show');
				var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')');
        		console.log(tab)
        		console.log('tab')
        		var seccion=$(tab).find('.resultado_tab')
        		console.log(seccion)
        		console.log('seccion')
        		var zona=$(seccion).find('.cargar')
        		console.log(zona)
        		console.log('zona')
				var enlace = form.find('#id_enlace').val();
				$(zona).load(enlace)
		    },
        	error : function(xhr,errmsg,err) {
        		$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                	" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        		console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        	}
		});
	};
	
});
$(document).ready(function() {
	
	function get_data(form){
		dataform = new FormData();
		console.log(form);
		var list = [];
		var cadena='';
		contador=0;
		form.find('input, textarea, select').each(function(){ 
			element=$(this);
			console.log(element);
			console.log(element.val());
			if ($(element).is('select')){
				console.log('select')
				dataform.append(element.attr('name'),form.find(':selected').val());
			}
			if (element.attr('name')=='image'){
				dataform.append('image', form.find('#id_image')[0].files[0]);
			}
			if($(element).is('input[type="checkbox"]')){
				if ($(element).is(":checked")){
					list.push(String(element.val())),
					console.log('checked')
					console.log(list)
				}
				console.log('elegido')
			}
			else{
				console.log('input')
				dataform.append(element.attr('name'), element.val());
			}
		
		});
		console.log(cadena)
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

	$(document).on("click","[class*=boton-apuntar-]",function(){
		var form = $(this).parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});
	
	$(document).on("click","[class*=boton-desapuntar-]",function(){
		var form = $(this).parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});

	$(document).on("submit","[class*=form-apuntar-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			var key = form.find('input:hidden[name=pk]').val();
			var tipe = form.find('input:hidden[name=tipe]').val();
			link(key, tipe, form);
			event.stopPropagation();
		});
	});
	
	$(document).on("submit","[class*=form-desapuntar-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			var key = form.find('input:hidden[name=pk]').val();
			var tipe = form.find('input:hidden[name=tipe]').val();
			unlink(key, tipe, form);
			event.stopPropagation();
		});
	});

	function link(key, tipe, form){
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')'); 
		console.log('change')
		console.log(tab)
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		var formularios = tab.find('.select_formulario');
		event.stopPropagation(); 
	    event.preventDefault(); 
		var clave = key;
		var apuntar = form.find('input:hidden[name=apuntar]').val();
		console.log(key);
		$.ajax({
			url : form.attr('action'),
			data : { 
				pk:parseInt(key),
				tipe:tipe,
				apuntar:apuntar,
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
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')');
    	console.log(tab)
    	console.log('tab')
    	var seccion=$(tab).find('.resultado_tab')
    	console.log(seccion)
    	var seccion_id='#' + String($(seccion).attr('id'))
    	console.log('seccion')
    	var zona=$(seccion).find('.cargar')
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		var sector = '#'+String($(zona).attr('id'))
		console.log(sector)
		console.log('sector')
		$(seccion).load('/sportcenter/clases/no_curso')
		$('#my-modal').modal('hide');
		console.log('fin change')
	};
	
	function unlink(key, tipe, form){
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')'); 
		console.log('change')
		console.log(tab)
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		var formularios = tab.find('.select_formulario');
		event.stopPropagation(); 
	    event.preventDefault(); 
		var clave = key;
		var desapuntar = form.find('input:hidden[name=desapuntar]').val();
		console.log(key);
		$.ajax({
			url : form.attr('action'),
			data : { 
				pk:parseInt(key),
				tipe:tipe,
				desapuntar:desapuntar,
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
				$('#my-modal-user').modal('hide');
		    },
		    error : function(xhr,errmsg,err) {
		    	$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
		    	" <a href='#' class='close'>&times;</a></div>"); 
		    	console.log(xhr.status + ": " + xhr.responseText);
		    }
		});
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')');
    	console.log(tab)
    	console.log('tab')
    	var seccion=$(tab).find('.resultado_tab')
    	console.log(seccion)
    	var seccion_id='#' + String($(seccion).attr('id'))
    	console.log('seccion')
    	var zona=$(seccion).find('.cargar')
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		var sector = '#'+String($(zona).attr('id'))
		console.log(sector)
		console.log('sector')
		$(seccion).load('/sportcenter/clases/mi_curso')
		$('#my-modal').modal('hide');
		console.log('fin change')
	};
	
});
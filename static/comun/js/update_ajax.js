$(document).ready(function() {
	
	function get_data(form){
		dataform = new FormData();
		form.find('input, textarea, select').each(function(){ 
			element=$(this);
			if (element.attr('name')=='image'){
				dataform.append('image', form.find('#id_image')[0].files[0]);
			}
			else{
				dataform.append(element.attr('name'), element.val());
			}
		});
	    console.log('dataform');
	    console.log(dataform);
		return dataform;
	}
	
	$("#id_image").on("change", function(){
		var file = $('#id_image')[0].files[0];
	});
	
	var procesando= function timeout_trigger(){
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init(){
		setTimeout(procesando, 3000);
	}

	$(document).on("click","[class*=boton-modificar-]",function(){
		var form = $(this).parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});

	$(document).on("click","[class*=boton_modificar_]",function(){
	    var form = $(this).parent().parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});
	
	$(document).on("submit","[class*=form-modificar-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			var key = form.find('input:hidden[name=pk]').val();
			var tipe = form.find('input:hidden[name=tipe]').val();
			change_element(key, tipe, form);
			event.stopPropagation();
		});
	});
	
	$(document).on("submit","[class*=formulario-modificar-datos-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			edit_element(form);
			event.stopPropagation();
		});
	});
	
	function change_element(key, tipe, form){
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')'); 
		console.log('change')
		console.log(tab)
		var enlace = form.find('#id_enlace').val();
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		var formularios = tab.find('.select_formulario');
		var formulario = formularios.find('[class*=div_formulario_modificar_]');
		var formulario_2 = formularios.find('[class*=div_formulario_crear_]');
		formulario_2.addClass('hide');
		formulario.removeClass('hide');
		var formulario_modificar=formulario.find('form');
		console.log(formulario_modificar)
		console.log(formulario)
		event.stopPropagation(); 
	    event.preventDefault(); 
		var clave = key;
		var cargar = form.find('input:hidden[name=cargar]').val();
		console.log(key);
		$.ajax({
			url : form.attr('action'),
			data : { 
				pk:parseInt(key),
				tipe:tipe,
				cargar:cargar,
			},
		    type: 'POST',
        	success : function(response_data) {
        				var html ='';
        				for (var key in response_data) {
        					if (response_data.hasOwnProperty(key)) {
              			  		console.log(key + " -> " + response_data[key]);
              			  		var local = String(key);
              			  		if (local != "image"){
              			  			formulario_modificar.find('#id_'+local).val(response_data[key]);
              			  		}
        					}
        				}
        				$('<input>').attr({type:'hidden',id:'element',name:'element',value:clave,}).appendTo(formulario_modificar);
        	},
        	error : function(xhr,errmsg,err) {
        		$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                	" <a href='#' class='close'>&times;</a></div>"); 
        		console.log(xhr.status + ": " + xhr.responseText);
        	}
		});
		console.log('fin change')
	};
	
	function edit_element(form){
		console.log('edit')
		event.stopPropagation();
	    event.preventDefault();
	    var key = form.find('input:hidden[name=element]').val();
		dataform=get_data(form);
		var enlace = form.find('#id_enlace').val();
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
                    html+='<h2 class="text-danger"><strong>Han ocurrido errores</strong></h2></div></div>';
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
                    html+='<h2 class="text-success"><strong>Modificacion realizada</strong></h2></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
            					html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
              				  	if (key != "Imagen"){
              				  		html+='<strong><p class="text-success">' + key + ": " + response_data[key] + '</p></strong>';
              				  	}
            					console.log(key + " -> " + response_data[key]);
              				  	html+='</div></div>';
              			  	}
            			}
            		}
            		html+='<br/>';
            		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')'); 
            		console.log(tab)
            		console.log('change')
            		var formularios = tab.find('.select_formulario');
            		console.log(formularios)
            		var formulario = formularios.find('[class*=div_formulario_modificar_]');
            		var texto= formulario.find("#id_enlace").val();
            		var formulario_2 = formularios.find('[class*=div_formulario_crear_]');
            		console.log(formulario)
            		console.log(formulario_2)
            		formulario.addClass('hide');
            		formulario_2.removeClass('hide');
        		}
        		$('.image_ajax').addClass('hide');
        		$('.info').append(html);
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
                	" <a href='#' class='close'>&times;</a></div>"); 
        		console.log(xhr.status + ": " + xhr.responseText);
        	}
		});
		
	};
	
});
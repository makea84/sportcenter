$(function() {
    $("#tabs").tabs();
  });

$(document).ready(function() {

	$(document).on("submit","[class*=formulario-crear-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			create_element(form);
			event.stopPropagation();
		});
	});
	
	$(document).on("click","[class*=boton_crear_]",function(){
	    var form = $(this).parent().parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});
	
	$("#id_image").on("change", function(){
		var file = $('#id_image')[0].files[0];
	});
	
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
	
	var procesando= function timeout_trigger() {
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init() {
	    setTimeout(procesando,3000);
	}
	
	function create_element(form) {
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')'); 
		console.log('create')
		console.log(tab)
		var enlace = form.find('#id_enlace').val();
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		var formularios = tab.find('.select_formulario');
		var formulario = formularios.find('[class*=div_formulario_crear_]');
		var formulario_crear=formulario.find('form');
		dataform=get_data(formulario_crear);
		event.stopPropagation(); 
	    event.preventDefault();
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
                    html+='<h2 class="text-success"><strong>Creacion realizada</strong></h2></div></div>';
            		for (var key in response_data) {
            			if(key != 'hay_error'){
            				if (response_data.hasOwnProperty(key)) {
            					html+='<div class="row"><div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">';
            					if (key != 'Imagen'){
            						html+='<strong><p class="text-success">' + key + ": " + response_data[key] + '</p></strong>';
            					}
            					else{
            						html+='<strong><p class="text-success">Imagen subida.</p></strong>';
            					}
            					
              				  	console.log(key + " -> " + response_data[key]);
              				  	
              				  	html+='</div></div>';
              			  	}
            			}
            		}
            		html+='<br/>';
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
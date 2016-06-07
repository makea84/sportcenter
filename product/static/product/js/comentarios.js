// ACTUAR SOBRE ELEMENTOS CARGADOS CON AJAX
$('.comentarioElegido').hide();
$(document).ajaxComplete(function(){
        
  // BOTON MODIFICAR EN FORMULARIO MODIFICAR
    $("#boton_Modificar_Comentario").click(function(event) { // for each edit contact url
	event.preventDefault();
	$("#form_Modificar_Comentario").submit(); 	
    });
	
    // SUBMIT FORMULARIO MODIFICAR
    $('#form_Modificar_Comentario').submit(function(event) {
	$('.comentarioElegido').hide();
	var input_string2 = $('#form_Modificar_Comentario').attr('action');
	event.preventDefault();
	var cadena = input_string2.split('/');
	console.log(cadena);
	var valor = cadena[cadena.length-2];
	console.log(valor);
	var input_string = $("input[id^='mi_comentario_']").val();
	console.log(input_string);
	$.ajax({
	    url : "/redetsii/comentarios/modificar/"+valor+"/",
	    type : "POST",
	    dataType: "json",
	    data : {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		name: $('#form_Modificar_Comentario #id_name').val(),
		description: $('#form_Modificar_Comentario #id_description').val(),
		expire: $('#form_Modificar_Comentario #id_expire').val(),
	    },
	    beforeSend: function () {
		$('.comentarioElegido').show();
            },
            success: function(result){
	        $('.comentarioElegido').html(result);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
		console.log(errmsg);
		console.log(err);
	    },
	});
	return false;
    });
    
    // BOTON CREAR EN FORMULARIO CREAR
    $("#boton_Crear_Comentario").click(function(event) { // for each edit contact url
	event.preventDefault();
	$("#form_Crear_Comentario").submit(); 	
    });
	
    // SUBMIT FORMULARIO CREAR
    $('#form_Crear_Comentario').submit(function(event) {
	$('.comentarioElegido').hide();
	event.preventDefault();
	var form=$('#form_Crear_Comentario');
	console.log(form.serialize());	
	$.ajax({
	    url : "/redetsii/comentarios/crear/",
	    type : "POST",
	    dataType: "json",
	    data : {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		name: $('#form_Crear_Comentario #id_name').val(),
		description: $('#form_Crear_Comentario #id_description').val(),
		expire: $('#form_Crear_Comentario #id_expire').val(),
	    },
	    beforeSend: function () {
		$('.comentarioElegido').show();
            },
            success: function(result){
        	$('.comentarioElegido').html(result);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
		console.log(errmsg);
		console.log(err);
	    },
	});
	return false;
    });
    
    $("input[id*='boton_Dejar_Comentario_']").on("click", function() {
    	var form = $(this).parent();
	var input_string = form.attr('action');
	var idComment = form.find('input[name="idComment"]').val();
	console.log(input_string);
	console.log(idComment);
	$.ajax({
	    url: input_string,
	    type: "POST",
	    dataType: "json",
	    data: {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		idComment: idComment,
	    },
	    beforeSend: function () {
		$('.comentarioElegido').show();
	    },
	    success: function(data){
		console.log(data);
		var imagen = $('.imagenUsuarioPlantilla').attr('src');
		var html= '';
		$('.recuperados_seguidos').html('');
		$('.recuperados_sugeridos').html('');
		var html2='';
		console.log("SUCCESS");
		var csrf = data.csrf;
		var data1 = data.sugeridos_list;
		console.log(data1);
		console.log( JSON.stringify(data1));
		var data2 = data.seguidos_list;
		console.log(data2);
		console.log( JSON.stringify(data2));
		for(var i=0; i<data1.length; i++) {
		    var dato = data1[i];
		    console.log(dato);
		    html+='<div class="sugerido_comentario">';
		    html+='<div class="row comentario_sugerido_envoltorio">';
		    html+='<div class="col-md-3 col-lg-3 col-sm-3">';
		    html+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		    html+='</div>';//fin 3	
		    html+='<div class="col-md-9 col-lg-9 col-sm-9">';
		    html+='<div class="row">';
		    html+='<div class="col-md-12 col-lg-12 col-sm-12">';
		    html+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato.pk + '">' + dato.fields.name + '</a>';
		    html+='</div>';//fin 12
		    html+='</div>';//fin row
		    html+='<div class="row">';	
		    html+='<form class="form formularioSeguir" id="form_Seguir_Comentario_' + dato.pk  + '" method="POST" action="/redetsii/comentarios/seguir/' + dato.pk  + '/">';
		    html+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		    html+='<input type="hidden" name="idComment" value="' + dato.pk + '">';
		    html+='<input id="boton_Seguir_Comentario_' + dato.pk + '" class="btn btn-primary" type="submit" name="seguir_comentario" value="Seguir" />';
		    html+='</form>';	
		    html+='</div>';//fin row
		    html+='</div>';//Fin 9	
		    html+='</div>';//fin grupo_sugerido_envoltorio
		    html+='</div>';//fin_sugerido_grupo
		 }
		 for(var j=0; j<data2.length; j++) {
		     var dato2 = data2[j];
		     console.log(dato2);
		     html2+='<div class="seguido_comentario">';
		     html2+='<div class="row comentario_seguido_envoltorio">';
		     html2+='<div class="col-md-3 col-lg-3 col-sm-3">';
		     html2+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		     html2+='</div>';//fin 3	
		     html2+='<div class="col-md-9 col-lg-9 col-sm-9">';
		     html2+='<div class="row">';
		     html2+='<div class="col-md-12 col-lg-12 col-sm-12">';
		     html2+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato2.pk + '">' + dato2.fields.name + '</a>';
		     html2+='</div>';//fin 12
		     html2+='</div>';//fin row
		     html2+='<div class="row">';	
		     html2+='<form class="form formularioDejar" id="form_Dejar_Comentario_' + dato2.pk  + '" method="POST" action="/redetsii/comentarios/dejar/' + dato2.pk  + '/">';
		     html2+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		     html2+='<input type="hidden" name="idComment" value="' + dato2.pk + '">';
		     html2+='<input id="boton_Dejar_Comentario_' + dato2.pk + '" class="btn btn-primary" type="submit" name="dejar_comentario" value="Dejar" />';
		     html2+='</form>';	
		     html2+='</div>';//fin row
		     html2+='</div>';//Fin 9	
		     html2+='</div>';//fin grupo_sugerido_envoltorio
		     html2+='</div>';//fin_sugerido_grupo
		}
		$('.recuperados_sugeridos').html(html);
		$('.recuperados_seguidos').html(html2);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
	    	console.log(errmsg);
	    	console.log(err);
	    },
	});
	return false;
    });
    
    $("input[id*='boton_Seguir_Comentario_']").on("click", function() {
    	var form = $(this).parent();
	var input_string = form.attr('action');
	var idComment = form.find('input[name="idComment"]').val();
	console.log(input_string);
	console.log(idComment);
	$.ajax({
	    url: input_string,
	    type: "POST",
	    dataType: "json",
	    data: {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		idComment: idComment,
	    },
	    beforeSend: function () {
		$('.comentarioElegido').show();
	    },
	    success: function(data){
		console.log(data);
		var imagen = $('.imagenUsuarioPlantilla').attr('src');
		var html= '';
		$('.recuperados_seguidos').html('');
		$('.recuperados_sugeridos').html('');
		var html2='';
		console.log("SUCCESS");
		var csrf = data.csrf;
		var data1 = data.sugeridos_list;
		console.log(data1);
		console.log( JSON.stringify(data1));
		var data2 = data.seguidos_list;
		console.log(data2);
		console.log( JSON.stringify(data2));
		for(var i=0; i<data1.length; i++) {
		    var dato = data1[i];
		    console.log(dato);
		    html+='<div class="sugerido_comentario">';
		    html+='<div class="row comentario_sugerido_envoltorio">';
		    html+='<div class="col-md-3 col-lg-3 col-sm-3">';
		    html+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		    html+='</div>';//fin 3	
		    html+='<div class="col-md-9 col-lg-9 col-sm-9">';
		    html+='<div class="row">';
		    html+='<div class="col-md-12 col-lg-12 col-sm-12">';
		    html+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato.pk + '">' + dato.fields.name + '</a>';
		    html+='</div>';//fin 12
		    html+='</div>';//fin row
		    html+='<div class="row">';	
		    html+='<form class="form formularioSeguir" id="form_Seguir_Comentario_' + dato.pk  + '" method="POST" action="/redetsii/comentarios/seguir/' + dato.pk  + '/">';
		    html+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		    html+='<input type="hidden" name="idComment" value="' + dato.pk + '">';
		    html+='<input id="boton_Seguir_Comentario_' + dato.pk + '" class="btn btn-primary" type="submit" name="seguir_comentario" value="Seguir" />';
		    html+='</form>';	
		    html+='</div>';//fin row
		    html+='</div>';//Fin 9	
		    html+='</div>';//fin grupo_sugerido_envoltorio
		    html+='</div>';//fin_sugerido_grupo
		 }
		 for(var j=0; j<data2.length; j++) {
		     var dato2 = data2[j];
		     console.log(dato2);
		     html2+='<div class="seguido_comentario">';
		     html2+='<div class="row comentario_seguido_envoltorio">';
		     html2+='<div class="col-md-3 col-lg-3 col-sm-3">';
		     html2+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		     html2+='</div>';//fin 3	
		     html2+='<div class="col-md-9 col-lg-9 col-sm-9">';
		     html2+='<div class="row">';
		     html2+='<div class="col-md-12 col-lg-12 col-sm-12">';
		     html2+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato2.pk + '">' + dato2.fields.name + '</a>';
		     html2+='</div>';//fin 12
		     html2+='</div>';//fin row
		     html2+='<div class="row">';	
		     html2+='<form class="form formularioDejar" id="form_Dejar_Comentario_' + dato2.pk  + '" method="POST" action="/redetsii/comentarios/dejar/' + dato2.pk  + '/">';
		     html2+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		     html2+='<input type="hidden" name="idComment" value="' + dato2.pk + '">';
		     html2+='<input id="boton_Dejar_Comentario_' + dato2.pk + '" class="btn btn-primary" type="submit" name="dejar_comentario" value="Dejar" />';
		     html2+='</form>';	
		     html2+='</div>';//fin row
		     html2+='</div>';//Fin 9	
		     html2+='</div>';//fin grupo_sugerido_envoltorio
		     html2+='</div>';//fin_sugerido_grupo
		}
		$('.recuperados_sugeridos').html(html);
		$('.recuperados_seguidos').html(html2);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
	    	console.log(errmsg);
	    	console.log(err);
	    },
	});
	return false;
    });
    
});

$('.comentarioElegido').hide();
// DOM CARGADO COMPLETAMENTE
$(document).ready(function(){
    
    $('.comentarioElegido').hide();
    
    $('#form_opciones input[name="opcion"]').click(function(){
	$('.comentarioElegido').show();
	var seleccion= $("#form_opciones input[name='opcion']:checked").val(); 
	console.log(seleccion);
	if (seleccion=='crear'){
	    $('#form_select_modificar').css('display','none');
    	    setTimeout(function(){
    		$('.comentarioElegido').load("/redetsii/comentarios/crear/");
    	    }, 2000);
	}
	else{
	    $('#form_select_modificar').css('display','block');
	}
    });
	
    $('#form_select_modificar>#select_modificar').change(function(){
	$('.comentarioElegido').hide();
	var seleccion= $('#form_select_modificar>#select_modificar');
	var opcion = seleccion.val();
	console.log(opcion);
	console.log('load');
	$('.comentarioElegido').show();
	setTimeout(function(){
	    $('.comentarioElegido').load("/redetsii/comentarios/modificar/"+opcion+'/');
	}, 2000);
    });
	
    $(".comentario_Recuperado").mouseover(function() { // for each edit contact url
        $(".oculto").removeClass('hide');
        return false; // prevent the click propagation
    });
    
    $(".comentario_Recuperado").mouseout(function() { // for each edit contact url
        $(".oculto").addClass('hide');
        return false; // prevent the click propagation
    });
    
    $('a[id*="mi_comentario_"]').each(function(){
    	this.click(function(){
    	$('.comentarioElegido').hide();
        event.preventDefault();
        var input_string = $(this).attr('href');
        var cadena = input_string.split('/');
        console.log(cadena);
        var valor = cadena[cadena.length-1];
        console.log(valor);
    	console.log(input_string);
        $.ajax({
            url: "/redetsii/comentarios/modificar/"+valor+"/",
            type: "POST",
            dataType: "json",
            data: {
    		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
    		client_response : valor,
            },
            beforeSend: function () {
    		$('.comentarioElegido').show();
            },
            success: function(data) {
    		var html="";
    		console.log("SUCCESS");
    		html+='<div class="modal-body">';
    		html+='<form class="form" id="form_Crear" method="post" action="/redetsii/comentarios/prueba_gestion/">';
    		for (var i=0;i<data.length;i++){
    		    html+='<div class="form-group" style="margin-bottom:3px;">';	
    		    html+= data.fields[i].titulo;
    		    html+='</div>';
    		    html+='<div class="form-group" style="margin-bottom:3px;">';	
    		    html+= data.fields[i].descripcion;
    		    html+='</div>';
    		    html+='<div class="form-group" style="margin-bottom:3px;">';	
    		    html+= data.fields[i].fecha_fin;
    		    html+='</div>';
    		}
    		html+='<input id="boton_Crear" class="btn btn-primary" type="submit" name="crear_comentario" value="Crear" />';
    		html+='</form>'; 
        	html+='</div>';    			
    		$('.comentarioElegido').html(html);
            },
            error: function(xhr,errmsg,err) {
    		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);
    		console.log(errmsg);
    		console.log(err);
            },
    	});
       	return false;
      });// FIN CLICK
    }); // FIN EACH
    
    $("input[id*='boton_Dejar_Comentario_']").click(function() {
    	var form = $(this).parent();
	var input_string = form.attr('action');
	var idComment = form.find('input[name="idComment"]').val();
	console.log(input_string);
	console.log(idComment);
	$.ajax({
	    url: input_string,
	    type: "POST",
	    dataType: "json",
	    data: {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		idComment: idComment,
	    },
	    beforeSend: function () {
		$('.comentarioElegido').show();
	    },
	    success: function(data){
		console.log(data);
		var imagen = $('.imagenUsuarioPlantilla').attr('src');
		var html= '';
		$('.recuperados_seguidos').html('');
		$('.recuperados_sugeridos').html('');
		var html2='';
		console.log("SUCCESS");
		var csrf = data.csrf;
		var data1 = data.sugeridos_list;
		console.log(data1);
		console.log( JSON.stringify(data1));
		var data2 = data.seguidos_list;
		console.log(data2);
		console.log( JSON.stringify(data2));
		for(var i=0; i<data1.length; i++) {
		    var dato = data1[i];
		    console.log(dato);
		    html+='<div class="sugerido_comentario">';
		    html+='<div class="row comentario_sugerido_envoltorio">';
		    html+='<div class="col-md-3 col-lg-3 col-sm-3">';
		    html+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		    html+='</div>';//fin 3	
		    html+='<div class="col-md-9 col-lg-9 col-sm-9">';
		    html+='<div class="row">';
		    html+='<div class="col-md-12 col-lg-12 col-sm-12">';
		    html+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato.pk + '">' + dato.fields.name + '</a>';
		    html+='</div>';//fin 12
		    html+='</div>';//fin row
		    html+='<div class="row">';	
		    html+='<form class="form formularioSeguir" id="form_Seguir_Comentario_' + dato.pk  + '" method="POST" action="/redetsii/comentarios/seguir/' + dato.pk  + '/">';
		    html+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		    html+='<input type="hidden" name="idComment" value="' + dato.pk + '">';
		    html+='<input id="boton_Seguir_Comentario_' + dato.pk + '" class="btn btn-primary" type="submit" name="seguir_comentario" value="Seguir" />';
		    html+='</form>';	
		    html+='</div>';//fin row
		    html+='</div>';//Fin 9	
		    html+='</div>';//fin grupo_sugerido_envoltorio
		    html+='</div>';//fin_sugerido_grupo
		 }
		 for(var j=0; j<data2.length; j++) {
		     var dato2 = data2[j];
		     console.log(dato2);
		     html2+='<div class="seguido_comentario">';
		     html2+='<div class="row comentario_seguido_envoltorio">';
		     html2+='<div class="col-md-3 col-lg-3 col-sm-3">';
		     html2+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		     html2+='</div>';//fin 3	
		     html2+='<div class="col-md-9 col-lg-9 col-sm-9">';
		     html2+='<div class="row">';
		     html2+='<div class="col-md-12 col-lg-12 col-sm-12">';
		     html2+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato2.pk + '">' + dato2.fields.name + '</a>';
		     html2+='</div>';//fin 12
		     html2+='</div>';//fin row
		     html2+='<div class="row">';	
		     html2+='<form class="form formularioDejar" id="form_Dejar_Comentario_' + dato2.pk  + '" method="POST" action="/redetsii/comentarios/dejar/' + dato2.pk  + '/">';
		     html2+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		     html2+='<input type="hidden" name="idComment" value="' + dato2.pk + '">';
		     html2+='<input id="boton_Dejar_Comentario_' + dato2.pk + '" class="btn btn-primary" type="submit" name="dejar_comentario" value="Dejar" />';
		     html2+='</form>';	
		     html2+='</div>';//fin row
		     html2+='</div>';//Fin 9	
		     html2+='</div>';//fin grupo_sugerido_envoltorio
		     html2+='</div>';//fin_sugerido_grupo
		}
		$('.recuperados_sugeridos').html(html);
		$('.recuperados_seguidos').html(html2);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
	    	console.log(errmsg);
	    	console.log(err);
	    },
	});
	return false;
    });
    
    $("input[id*='boton_Seguir_Comentario_']").click(function() {
    	var form = $(this).parent();
	var input_string = form.attr('action');
	var idComment = form.find('input[name="idComment"]').val();
	console.log(input_string);
	console.log(idComment);
	$.ajax({
	    url: input_string,
	    type: "POST",
	    dataType: "json",
	    data: {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		idComment: idComment,
	    },
	    beforeSend: function () {
		$('.comentarioElegido').show();
	    },
	    success: function(data){
		console.log(data);
		var imagen = $('.imagenUsuarioPlantilla').attr('src');
		var html= '';
		$('.recuperados_seguidos').html('');
		$('.recuperados_sugeridos').html('');
		var html2='';
		console.log("SUCCESS");
		var csrf = data.csrf;
		var data1 = data.sugeridos_list;
		console.log(data1);
		console.log( JSON.stringify(data1));
		var data2 = data.seguidos_list;
		console.log(data2);
		console.log( JSON.stringify(data2));
		for(var i=0; i<data1.length; i++) {
		    var dato = data1[i];
		    console.log(dato);
		    html+='<div class="sugerido_comentario">';
		    html+='<div class="row comentario_sugerido_envoltorio">';
		    html+='<div class="col-md-3 col-lg-3 col-sm-3">';
		    html+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		    html+='</div>';//fin 3	
		    html+='<div class="col-md-9 col-lg-9 col-sm-9">';
		    html+='<div class="row">';
		    html+='<div class="col-md-12 col-lg-12 col-sm-12">';
		    html+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato.pk + '">' + dato.fields.name + '</a>';
		    html+='</div>';//fin 12
		    html+='</div>';//fin row
		    html+='<div class="row">';	
		    html+='<form class="form formularioSeguir" id="form_Seguir_Comentario_' + dato.pk  + '" method="POST" action="/redetsii/comentarios/seguir/' + dato.pk  + '/">';
		    html+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		    html+='<input type="hidden" name="idComment" value="' + dato.pk + '">';
		    html+='<input id="boton_Seguir_Comentario_' + dato.pk + '" class="btn btn-primary" type="submit" name="seguir_comentario" value="Seguir" />';
		    html+='</form>';	
		    html+='</div>';//fin row
		    html+='</div>';//Fin 9	
		    html+='</div>';//fin grupo_sugerido_envoltorio
		    html+='</div>';//fin_sugerido_grupo
		 }
		 for(var j=0; j<data2.length; j++) {
		     var dato2 = data2[j];
		     console.log(dato2);
		     html2+='<div class="seguido_comentario">';
		     html2+='<div class="row comentario_seguido_envoltorio">';
		     html2+='<div class="col-md-3 col-lg-3 col-sm-3">';
		     html2+='<img class="imagenUsuarioPlantilla" src="' + imagen + '" alt="imagen de usuario">';
		     html2+='</div>';//fin 3	
		     html2+='<div class="col-md-9 col-lg-9 col-sm-9">';
		     html2+='<div class="row">';
		     html2+='<div class="col-md-12 col-lg-12 col-sm-12">';
		     html2+='<a class="comentario" href="/redetsii/comentarios/consultar/'+ dato2.pk + '">' + dato2.fields.name + '</a>';
		     html2+='</div>';//fin 12
		     html2+='</div>';//fin row
		     html2+='<div class="row">';	
		     html2+='<form class="form formularioDejar" id="form_Dejar_Comentario_' + dato2.pk  + '" method="POST" action="/redetsii/comentarios/dejar/' + dato2.pk  + '/">';
		     html2+='<input type="hidden" value="' + csrf + ' +" name="csrfmiddlewaretoken">';
		     html2+='<input type="hidden" name="idComment" value="' + dato2.pk + '">';
		     html2+='<input id="boton_Dejar_Comentario_' + dato2.pk + '" class="btn btn-primary" type="submit" name="dejar_comentario" value="Dejar" />';
		     html2+='</form>';	
		     html2+='</div>';//fin row
		     html2+='</div>';//Fin 9	
		     html2+='</div>';//fin grupo_sugerido_envoltorio
		     html2+='</div>';//fin_sugerido_grupo
		}
		$('.recuperados_sugeridos').html(html);
		$('.recuperados_seguidos').html(html2);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
	    	console.log(errmsg);
	    	console.log(err);
	    },
	});
	return false;
    });
    
    $("#botonComentar").click(function() {
    	var form = $(this).parent();
	var input_string = form.attr('action');
	console.log(input_string);
	var content = form.find('textarea[name="texto_comentario"]').val();
	var idEvent = form.find('input[name="idEvent"]').val();
	var idUserGroup= form.find('input[name="idUserGroup"]').val();
	console.log(content);
	$.ajax({
	    url: input_string,
	    type: "POST",
	    dataType: "json",
	    data: {
		csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
		content: content,
		idEvent: idEvent,
		idUserGroup: idUserGroup,
	    },
	    beforeSend: function () {
		//$('.comentarioElegido').show();
	    },
	    success: function(data){
		console.log(data);
		console.log(typeof(data))
		var html= '';
		console.log("SUCCESS");
		var data1 = data.comentario;
		console.log(data1);
		console.log( JSON.stringify(data1));
		var escritor="";
		var comentario="";
		var fecha="";
		var grupo="";
		var evento="";
		var elemento = $('.no_comentario');
		console.log(elemento);
		if($('.no_comentario').length){
		   console.log('primer'); 
		   $('.no_comentario').remove();   
		}
		for(var key in data1) {
		    console.log("clave " + key);
		    console.log(JSON.stringify(key));
		    // Check for proper key in dictionary
		    if (key in {escritor: 1, comentario: 1, id: 1, fecha: 1, grupo: 1, evento: 1}) {
			if(key==='escritor')
			    escritor=data1[key];
			if(key==='comentario')
			    comentario = data1[key];
			if(key==='fecha')
			    fecha = data1[key];
			if(key==='grupo')
			    grupo = data1[key];
			if(key==='evento')
			    evento = data1[key];
			var dato = data1[key];
			console.log(dato);
		    }
		    
		}
		html+='<div class="row columnaGrupo comentarioGrupo">';
		html+='<div class="col-md-12 col-lg-12 col-sm-12 comentario_este">';
		html+='<div class="col-md-12 col-lg-12 col-sm-12">';
		if (grupo !='') {
		    html+='<p class="textoGrupo"><b>Escritor</b> ' + escritor + '<b> Grupo</b> ' + grupo + ' ' + fecha + '</p>';
		    html+='<p class="textoGrupo">'+ comentario + '</p>';
		}
		if (evento !='') {
		    html+='<p class="textoEvento"><b>Escritor</b> ' + escritor + '<b> Evento</b> ' + evento + ' ' + fecha + '</p>';
		    html+='<p class="textoEvento">'+ comentario + '</p>';
		}
		else{
		    html+='<p class="textoUsuario"><b>Escritor</b> ' + escritor + ' ' + fecha + '</p>';
		    html+='<p class="textoUsuario">'+ comentario + '</p>';
		}
		
		html+='</div>';
		html+='</div>';
		html+='</div>';
		$('#comentarios').prepend(html);
	    },
	    error : function(xhr,errmsg,err) {
		$('.comentarioElegido').html(xhr.status + ": " + xhr.responseText);	
	    	console.log(errmsg);
	    	console.log(err);
	    },
	});
	return false;
    });
    
    var socket = io.connect("localhost", {port: 8002});

    socket.on('comentar', function(data) {
        var html= '';
	console.log("SUCCESS");
	var data1 = data.comentario;
	console.log(data1);
	console.log( JSON.stringify(data1));
	var escritor="";
	var comentario="";
	var elemento = $('.no_comentario');
	console.log(elemento);
	if($('.no_comentario').length){
	   console.log('primer'); 
	   $('.no_comentario').remove();   
	}
	for(var key in data1) {
	    console.log("clave " + key);
	    console.log(JSON.stringify(key));
	    // Check for proper key in dictionary
	    if (key in {escritor: 1, comentario: 1, id: 1,}) {
		if(key==='escritor')
		    escritor=data1[key];
		if(key==='comentario')
		    comentario = data1[key];
		var dato = data1[key];
		console.log(dato);
	    }
	    
	}
	html+='<div class="row columnaGrupo">';
	html+='<div class="col-md-12 col-lg-12 col-sm-12 comentario_este">';
	html+='<div class="col-md-12 col-lg-12 col-sm-12">';
	html+='<h4 class="subtitularPrincipal"><b>Escritor</b> ' + escritor + '<br/>' + comentario + '</h4>';
	html+='</div>';
	html+='</div>';
	html+='</div>';
	$('#comentarios').prepend(html);
    });
});
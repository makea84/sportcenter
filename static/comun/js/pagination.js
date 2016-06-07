$(document).ready(function() {

	$(document).on("click","[class*=siguiente]",function(event){
		event.preventDefault();
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')');
    	console.log(tab)
    	console.log('tab')
    	var seccion=$(tab).find('.resultado_tab')
    	console.log(seccion)
    	var seccion_id='#' + String($(seccion).attr('id'))
    	console.log('seccion')
    	var zona=$(seccion).find('.cargar')
    	console.log(zona)
    	console.log('zona')
    	var pagination = $(zona).find('.pagination')    		
    	console.log(pagination)
    	var enlace = $(pagination).find('.siguiente')
    	console.log(enlace)
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		var sector = '#'+String($(zona).attr('id'))
		console.log(sector)
		console.log('sector')
		$(seccion).load($(enlace).attr('href')+' '+sector )
		$('#my-modal').modal('hide');
		event.stopPropagation();
	});

	$(document).on("click","[class*=anterior]",function(event){
		event.preventDefault();
		var tab =$('#tabs').find('>div:nth-of-type(' + ($('#tabs').tabs("option", "active") + 1) + ')');
    	console.log(tab)
    	console.log('tab')
    	var seccion=$(tab).find('.resultado_tab')
    	console.log(seccion)
    	var seccion_id='#' + String($(seccion).attr('id'))
    	console.log('seccion')
    	var zona=$(seccion).find('.cargar')
    	console.log(zona)
    	console.log('zona')
    	var pagination = $(zona).find('.pagination')    		
    	console.log(pagination)
    	var enlace = $(pagination).find('.anterior')
    	console.log(enlace)
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		var sector = '#'+String($(zona).attr('id'))
		console.log(sector)
		console.log('sector')
		$(seccion).load($(enlace).attr('href')+' '+sector )
		$('#my-modal').modal('hide');
		event.stopPropagation();
	});
	
	var procesando= function timeout_trigger() {
		$('.image_ajax').removeClass('hide');
	}
	
	function timeout_init() {
	    setTimeout(procesando,3000);
	}
	
	var limpiar= function timeout_trigger(id) {
		$(document).find('[class*=sin]').remove();
	}
	
	function timeout_init2(id) {
	    setTimeout(limpiar(id),1000);
	}
	
});
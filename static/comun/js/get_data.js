$(document).ready(function() {

	$(document).on("click","[class*=activo_li]>a",function(event){
		var hijo = $(this);
		console.log('click tab');
		var nombre = hijo.attr('href');
		var div = nombre.slice(1, nombre.length);
		var seccion = $('#'+div).find(".resultado_tab");
		console.log(div)
		console.log('tab')
		console.log(seccion)
		console.log('seccion')
		var cargar = $(seccion).find('.cargar')
		console.log(cargar)
		console.log('cargar')
		$(cargar).load($(this).attr('href') + ' #' + $(cargar).attr('id'))
	});

});
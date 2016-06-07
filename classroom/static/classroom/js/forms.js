$(document).ready(function() {

	$(document).on("click","[class*=activo_li]",function(event){
		var hijo = $(this).find('a');
		var nombre = hijo.attr('href');
		console.log(nombre)
		var sector = $(nombre).find(".select_formulario");
		console.log(sector)
		var sector_id=$(sector).attr('id');
		$(sector).find('.info').empty();
		console.log(sector_id)
		var parte =$(nombre).find('.cargar').parent()
		hijo.on("click", function(event){
			console.log('click tab');
			if((sector_id=='form_participacion') || (sector_id==='form_lugar')){
				$(sector).load('/sportcenter/clases/'+sector_id+'/ #'+sector_id)
				console.log('ok')
			}		
		});
	});
	
});
$(document).ready(function() {
	
	function get_data(form){
		dataform = new FormData();
		form.find('input, textarea, select').each(function(){ 
			element=$(this);
			dataform.append(element.attr('name'), element.val());
			console.log(element.val())
		});
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

	$(document).on("click","[class*=boton-descargar-]",function(event){
		var form = $(this).parent();
		console.log(form);
		event.preventDefault();
		event.stopPropagation();
		form.submit();
	});

	$(document).on("submit","[class*=form-descargar-]",function(event){
		$(this).each(function(){
			event.preventDefault();
			var form = $(this);
			change_element(form);
			event.stopPropagation();
		});
	});

	function change_element(form){
		console.log('change')
		$('.info').empty();
		$('.image_ajax').removeClass('hide');
		$('#my-modal').modal('show');
		timeout_init();
		$('#my-modal').modal('hide');
		dataform = get_data(form)
		$.ajax({
			url : $(form).attr('action'), 
			data:$(form).serialize(),
			type: 'POST',
			success: function(data) {
	            var blob=new Blob([data]);
	            var link=document.createElement('a');
	            link.href=window.URL.createObjectURL(blob);
	            link.download="Programa.pdf";
	            link.click();
	        },
        	error : function(xhr,errmsg,err) {
        		$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                	" <a href='#' class='close'>&times;</a></div>"); 
        		console.log(xhr.status + ": " + xhr.responseText);
        	}
		});
		console.log('fin change')
	};
	
});
$(document).ready(function() {
	
	var procesando= function timeout_trigger() {
		load_classroom();
	}
	
	function timeout_init() {
	    setTimeout(procesando,15000);
	}
	
	function load_classroom(){
		console.log('Prueba');
		prueba=$(".resultado").load("{% url 'otros' %}");
		console.log(prueba);
	}
	
	timeout_init();
	
});
<?php
	include_once "../webhook/somosioticos_dialogflow.php";
	credenciales('hammy','123456789');
	
	$mysqli =mysqli_connect("160.153.92.73", "ew987hm6p7os","Callofduty1.","clientesbodega");
	
	if(!$mysqli){
	echo "Error: No se pudo conectar a MySQL." . PHP_EOL;
	die();
	
	}		
	
	
	if (intent_recibido("consultar_cliente")){
	
		$no_cl = obtener_variables()['no_cl'];		
		$resultado= $mysqli->query("SELECT * FROM `clientes` WHERE `id_cliente` = $no_cl");
		$clientes =mysqli_fetch_assoc($resultado);
		$id_cliente = $clientes['id_cliente'];
		$estado = $clientes['estado'];
		$ruta =$clientes['ruta'];
		$bodega = $clientes['bodega'];
		
		enviar_texto("el cliente $id_cliente esta en estado $estado pertenece a la ruta $ruta y a la bodega $bodega ");
		
	}
	
	
	
	
	if (intent_recibido("calcular")){
	
		$valor1 = obtener_variables()['numero1'];
		$valor2 = obtener_variables()['numero2'];
		$resultado = $valor1 + $valor2;
		enviar_texto("el resultado es $resultado");
	}
	
	

?>

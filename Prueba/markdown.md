# Laboratorio 3: Capa de Transporte

Estos gráficos son resultado de un análisis que se hace sobre una simulación de 200 segundos descripta en el pdf de las consignas. 

Los parámetros fijos que utilizamos fueron los siguientes:
Tamaño de los paquetes (en bytes) = 12500
- Del nodo transmisor:
	Tamaño del buffer = 2000000
	Tiempo de servicio en la queue = exponential(0.1)
- Queue entre nodos:
	Tamaño del buffer = 200
	Tiempo de servicio en la queue = exponential(0.001)
- Del nodo receptor:
	Tamaño del buffer = 2000000
	Tiempo de servicio en la queue = exponential(0.1)

//Datarate = {}
//Más datarate + perdida de paquetes.

La diferencia entre los gráficos nace de modificar el intervalo de generación de los paquetes a través de la manipulación del parámetro GenerationInterval, al cuál se le fue asignando exponential(1), exponential(0.8), exponential(0.6), exponential(0.4), exponential(0.4) y exponential(0.1)

Una de las primeras diferencias que notamos es que a medida que aumentábamos la velocidad de la generación de paquetes, también crecía la utilización de los buffers (sobre todo el del nodo receptor).
Otra situación que notamos es que también aumenta la demora desde que un paquete es generado y trasmitido por la compuerta out del sink (es decir, desde que un paquete nace hasta que recorre todo el circuito que implementamos) a medida que aumenta la velocidad de generación de paquetes. Esto se debe a que los buffers se congestionan, produciendo el fenómeno del cuello de botella. La consecuencia inmediata de esta situación la pérdida de paquetes.

Los valores para las tasas y demoras de Transmisión fueron:

-Del NodoTx al Queue: el Datarate 1 Mbps con un Delay de 100 microsegundos.
-Del Queue al NodoRx: el Datarate 1 Mbps con un Delay de 100 microsegundos. 
-Del Queue al Sink: el Datarate 0.5 Mbps


Para el segundo caso los parámetros de los buffers, paquetes y GenerationInterval fueron los mismos, exceptuando las tasas y demoras de Transmisión. Las cuales las mismas fueron reasignadas con los siguientes valores:

-Del NodoTx al Queue: el Datarate 1 Mbps con un Delay de 100 microsegundos.
-Del Queue al NodoRx: el Datarate 0.5 Mbps con un Delay de 100 microsegundos. 
-Del Queue al Sink: el Datarate 1 Mbps

Entre los respectivos gŕaficos, podemos observar que las perdidas de paquetes son parecidas. Por lo cuál concluimos que en ambas ocasiones se encuentra un problema parecido de pérdidas de paquetes.

A continuación se observan los gráficos para el caso de estudio Nro. 1 y Nro. 2 con sus respectivos valores mencionados anteriormente, con
GenerationInterval con un valor de `exponential(0.1)`

![Caso de Estudio 2](/img_estudio_2/generationInterval01.jpg "generationInterval01.jpg")

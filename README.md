# Urban Routes Automation Testing

Presentado por: Juliana Gavilan del grupo 19 de QA Engineer

## Descripción del Proyecto

Este proyecto fue diseñado para la realización pruebas automatizadas
sobre la aplicación Urban Routes, 
que es una plataforma para la solicitud de taxis con diferentes opciones de vehículos. 
Las pruebas cubren la configuración de la ruta a seguir por parte del 
usuario, la selección de la tarifa flash, en el tipo de vehículo confort,
la información del número de teléfono junto con la confirmación por código del mismo, 
El registro de un método de pago en este caso tarjeta, pasando por la solicitud al conductor por medio de un comentario,
la solicitud de pañuelos y mantas además de dos helados, para finalizar con la solicitud del vehículo al sistema.

## Tecnologías Utilizadas

### Python: 
Lenguaje de programación principal utilizado por su simplicidad y legibilidad.

### Selenium: 
Es una herramienta de código abierto que se utiliza para automatizar en navegadores web en este caso en particular con Google Chrome. 


### Pytest: 
Es un Framework de pruebas que facilita la creación y ejecución de las mismas en Python.

### GitHub: 
Es una plataforma de desarrollo colaborativo que nos permite gestionar las diferentes versiones del código fuente, lo cual nos permite llevar un control sobre los cambios que realizamos.

### WebDriver: 
Es una parte fundamental de Selenium que se encarga de interactuar directamente con el navegador web en la ejecución de las pruebas.

### JSON: 
Es un formato de intercambio de datos ligero y fácil de usar usado para manejar las respuestas de la API en el proceso de obtención del código de confirmación del número telefónico.

## Instrucciones para Ejecutar las Pruebas

Instala las dependencias necesarias: Selenium, Pytest 



El primer paso para el uso de esta automatización es el ingreso de una URL cuyo servidor este inicializado. En data y más específicamente en la variable urban_routes_url

Esta automatización cuenta con 4 pruebas seccionadas de la siguiente manera

La primera orientada a establecer la ruta inicial del trayecto aporta las direcciones desde donde se inicia a donde finaliza el recorrido.
La segunda realiza las diferentes solicitudes a los requerimientos propios del tipo de vehículo que selecciona.
La tercera agrega el número de celular realizando la confirmación por medio del código que genera el programa
La cuarta y última agrega el método de pago en este caso tarjeta.
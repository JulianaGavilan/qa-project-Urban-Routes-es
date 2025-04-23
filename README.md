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

<img decoding="async" 
     src="https://img.shields.io/badge/DevTools-FADADD?style=for-the-badge&logo=Drawio&logoColor=white" 
     alt="Drawio"/>
<img decoding="async" 
     src="https://img.shields.io/badge/Python-E6E6FA?style=for-the-badge&logo=python&logoColor=white" 
     alt="python"/>
<img decoding="async" 
     src="https://img.shields.io/badge/PyCharm-B2E0F7?&style=for-the-badge&logo=PyCharm&logoColor=white" 
     alt="PyCharm"/>
<img decoding="async" 
     src="https://img.shields.io/badge/Git_Bash-FFFACD?&style=for-the-badge&logo=GitBash&logoColor=white" 
     alt="GitBash"/>
<img decoding="async" 
     src="https://img.shields.io/badge/GitHub-C1F0DC?&style=for-the-badge&logo=GitHub&logoColor=white" 
     alt="GitHub"/>
<img decoding="async"
     src="https://img.shields.io/badge/Selenium-FFDAB9?style=for-the-badge&logo=Selenium&logoColor=white" 
     alt="Selenium"/>
<img decoding="async" 
     src="https://img.shields.io/badge/Pytest-AEDFF7?style=for-the-badge&logo=pytest&logoColor=white" 
     alt="pytest"/>
<img decoding="async"
     src="https://img.shields.io/badge/Pip-FFB6B9?style=for-the-badge&logo=Pip&logoColor=white" 
     alt="Pip"/>


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
El segundo paso es abrir la terminal y poner el siguiente comando 

#### Prueba 1  

pytest Test.py::TestUrbanRoutes::test_set_route 

#### Prueba 2  

pytest Test.py::TestUrbanRoutes::test_for_ice_creams

#### Prueba 3  

pytest Test.py::TestUrbanRoutes::test_message_for_driver

#### Prueba 4  

pytest Test.py::TestUrbanRoutes::test_add_phone

#### Prueba 5  

pytest Test.py::TestUrbanRoutes::test_add_new_payment

#### Prueba 6  

pytest Test.py::TestUrbanRoutes::test_comfort_tariff

#### Prueba 7  

pytest Test.py::TestUrbanRoutes::test_for_blankets_and_tissue

#### Prueba 8  

pytest Test.py::TestUrbanRoutes::test_to_modal_taxi

#### Prueba 9  

pytest Test.py::TestUrbanRoutes::test_for_final_form

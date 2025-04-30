# Urban Routes Automation Testing

Presentado por: Juliana Gavilan del grupo 19 de QA Engineer

## Descripción del Proyecto

[![Urban-Routes.png](https://i.postimg.cc/Gh3s2VXc/Urban-Routes.png)](https://postimg.cc/9zSfg83S)

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


## 🧰 Tecnologías Utilizadas

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

## :computer: Instrucciones para Ejecutar las Pruebas

1. Instala las dependencias necesarias: Selenium, Pytest 
2. El siguiente paso para el uso de esta automatización es el ingreso de una URL cuyo servidor este inicializado. En data y más específicamente en la variable urban_routes_url
3. En este paso se abre la terminal y se pone uno de los siguientes comandos de acuerdo a la prueba que se quiera ejecutar
   

#### Prueba 1  

pytest Test.py::TestUrbanRoutes::test_set_route 

En esta prueba se realizan las comprobaciones que corresponden a los campos de direccion. Haciendo uso de .send_keys() y .get_property()

[![prueba-1-Urban-routes.png](https://i.postimg.cc/pVJFPRYG/prueba-1-Urban-routes.png)](https://postimg.cc/Hjjx2GNX)

#### Prueba 2  

pytest Test.py::TestUrbanRoutes::test_for_ice_creams

En esta prueba se comprueban la cantidad de helados solicitados. Para obtener la informacion se utilizo .click() y .text

[![prueba-Helados.png](https://i.postimg.cc/MKtVmqnM/prueba-Helados.png)](https://postimg.cc/BXLjqWc4)

#### Prueba 3  

pytest Test.py::TestUrbanRoutes::test_message_for_driver

En esta pruba se evalua el mensaje al conductor. Utilizando .send_keys() y .get_property('value')

[![Prueba-3-Urban-routes.png](https://i.postimg.cc/C1jfBgyK/Prueba-3-Urban-routes.png)](https://postimg.cc/wyjBZnjK)

#### Prueba 4  

pytest Test.py::TestUrbanRoutes::test_add_phone

Esta prueba confirma el numero de telefono agregado. Utilizando .get_property('value')

[![prueba-4-Urban-Routes.png](https://i.postimg.cc/SRd2dfxF/prueba-4-Urban-Routes.png)](https://postimg.cc/2LqS8vW2)

#### Prueba 5  

pytest Test.py::TestUrbanRoutes::test_add_new_payment

Esta prueba comprueba la informacion de la tarjeta agregada la cual es su numero y codigo. Utilizando .get_property('value')

[![Prueba-5-Urban-Routes.png](https://i.postimg.cc/QtLTdMyP/Prueba-5-Urban-Routes.png)](https://postimg.cc/B8g6hJsc)

#### Prueba 6  

pytest Test.py::TestUrbanRoutes::test_comfort_tariff

En esta prueba se revisa que la tarifa seleccionada corresponda al modo comfort. Utilizando .text

[![prueba-2-Urban-Routes.png](https://i.postimg.cc/Zn4v6MZx/prueba-2-Urban-Routes.png)](https://postimg.cc/njSLJTXX)

#### Prueba 7  

pytest Test.py::TestUrbanRoutes::test_for_blankets_and_tissue

En esta prueba se revisa que la seleccion de manta y pañuelos se encuentre seleccionada. Se utiliza .get_property('checked') y .click()

[![prueba-7-Urban-Routes.png](https://i.postimg.cc/g0LhphN8/prueba-7-Urban-Routes.png)](https://postimg.cc/DWF0dSVw)

#### Prueba 8  

pytest Test.py::TestUrbanRoutes::test_to_modal_taxi

En esta prueba se revisa que aparezca el modal relacionado con la solicitud del vehiculo luego de llenar todo el formulario. Se utiliza .text

[![prueba-modal.png](https://i.postimg.cc/K8HTCfrm/prueba-modal.png)](https://postimg.cc/pmKyFD6S)

#### Prueba 9  

pytest Test.py::TestUrbanRoutes::test_for_final_form

En esta ultima prueba se confirma la informacion del taxi que llegara una vez se realice la espera correspondiente del servicio 

[![prueba-final-Urban-routes.png](https://i.postimg.cc/rwmWh34h/prueba-final-Urban-routes.png)](https://postimg.cc/HVqVnSB5)

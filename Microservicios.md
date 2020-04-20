[**Universidad Distrital Francisco José de
Caldas**]{lang="es-ES-u-co-trad"}

[**Facultad de Ingeniería**]{lang="es-ES-u-co-trad"}

[**Especialización en Ingeniería de Software**]{lang="es-ES-u-co-trad"}

[**Asignatura de Informática 1**]{lang="es-ES-u-co-trad"}

[**Docente: Alejandro Paolo Daza**]{lang="es-ES-u-co-trad"}

![](Microservicios_html_670be77737dc3351.png){width="197" height="197"}

\

  ---------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------
  **[Nombre: ]{lang="es-ES-u-co-trad"}**[[Angee Paola Ballesteros Maldonado]{style="font-weight: normal"}]{lang="es-ES-u-co-trad"}   **[Código: ]{lang="es-ES-u-co-trad"}**[[20201099027]{style="font-weight: normal"}]{lang="es-ES-u-co-trad"}
  **[Nombre: ]{lang="es-ES-u-co-trad"}**[[Luigi Santiago Fajardo Toloza]{style="font-weight: normal"}]{lang="es-ES-u-co-trad"}       [**Código:**]{lang="es-ES-u-co-trad"}[ 20201099029]{lang="es-ES-u-co-trad"}
  **[Nombre: ]{lang="es-ES-u-co-trad"}**[[Jeisson Jair Ariza Pulido]{style="font-weight: normal"}]{lang="es-ES-u-co-trad"}           [**Código:** ]{lang="es-ES-u-co-trad"}[20201099026]{lang="es-ES-u-co-trad"}
  ---------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------

\

[**Diseño de un aplicativo aritmético mediante el uso de Microservicios
con el Framework Flask**]{lang="es-ES-u-co-trad"}

[**Requerimiento:**]{lang="es-ES-u-co-trad"}[ Se plantea establecer una
arquitectura orientada a microservicios usando el micro-framework flask
para ofrecer la implementación de los servicios de suma, resta,
multiplicación y división. En el repositorio se deben exponer las
tecnologías seleccionadas para ofrecer los servicios propios de este
tipo de arquitecturas teniendo en cuenta que las operaciones se ofrecen
con flask. La explicación de despliegue, así como la explicación de las
herramientas seleccionadas debe ser clara en el README del
proyecto.]{lang="es-ES-u-co-trad"}

[**Procedimiento:** ]{lang="es-ES-u-co-trad"}[Inicialmente debemos
conocer que Flask es un micro-framework de Python, por este motivo
debemos tener instalado y de manera funcional Python 3 en la maquina en
la cual se va a desarrollar el requerimiento. Este procedimiento puede
ser consultado en \[1\], adicional a esto, si se va a trabajar en una
maquina con un SO basado en Linux(i.e. Mac OS o las distribuciones de
Linux), se sugiere que aplique el cambio de alias para
Python.]{lang="es-ES-u-co-trad"}

[Para el desarrollo de los servicios se utilizará el IDE Visual Studio
Code, dicho IDE permite integrar todos los componentes necesarios de
Python para el correcto desarrollo del requerimiento.
]{lang="es-ES-u-co-trad"}

[Se solicita la creación de 4 servicios para cada una de las operaciones
aritméticas(suma, resta, multiplicación y división), adicionalmente se
requiere un aplicativo web que permita consumir cada uno de estos
servicios cuando el usuario lo solicite. ]{lang="es-ES-u-co-trad"}

[Antes de iniciar debemos saber el porqué se utiliza Flask como
micro-framework de nuestro requerimiento, además debemos mencionar el
uso de herramientas adicionales como son Flask-CORS para el intercambio
de recursos de origen cruzado, Request Flask para el contenido que un
cliente web manda para almacenar al servidor, Waitress para el Web
Server Gateway Interface, por ultimo, Docker, utilizado para
]{lang="es-ES-u-co-trad"}[e]{lang="es-ES-u-co-trad"}[l despliegue
de ]{lang="es-ES-u-co-trad"}[[[aplicaciones]{style="text-decoration: none"}]{lang="es-ES-u-co-trad"}](https://es.wikipedia.org/wiki/Aplicaci%C3%B3n_inform%C3%A1tica)[ dentro
de ]{lang="es-ES-u-co-trad"}[[[contenedores de
software]{style="text-decoration: none"}]{lang="es-ES-u-co-trad"}](https://es.wikipedia.org/wiki/Contenedores_de_software)[.
A continuación, se especifican las características que nos llevaron a la
elección de estas herramientas, de igual manera en los casos en los que
consideramos necesario se adjuntan estrategias para la implementación de
estas herramientas. ]{lang="es-ES-u-co-trad"}

1.  [**Flask:**]{lang="es-ES-u-co-trad"}[ este micro-framework permite
    construir aplicaciones web y servicios Restful con Python de una
    manera simple, de forma tal que utilizando pocas líneas podemos
    llegar a tener un servicio Restful funcionando correctamente. Se
    podría decir que su mayor característica consiste en que permite
    crear rutas web de una forma muy sencilla. Entre sus características
    principales tenemos que, al ser micro, nos permite que en una sola
    pagina se pueda alojar una aplicación web. ]{lang="es-ES-u-co-trad"}

    1.  [**Instalación de Flask:**]{lang="es-ES-u-co-trad"}[ como se
        mencionaba previamente, es imprescindible contar con una
        instalación de Python en nuestra maquina de desarrollo, esto
        debido a que Flask es un micro-framework de Python y además su
        instalación se realiza mediante el administrador de paquetes de
        Python (pip). Es por esto que el primer paso y la mayoría de las
        instalaciones utilizadas en el desarrollo de este requerimiento
        se hacen mediante pip. Para instalar flask debemos ejecutar la
        siguiente línea en nuestra terminal
        ]{lang="es-ES-u-co-trad"}[**\$ pip install
        Flask**]{lang="es-ES-u-co-trad"}[. Por otra parte, es
        recomendable que cada proyecto se ejecute en un entorno virtual
        independiente para garantizar que no afecte ni sea afectado por
        otros proyectos, para esto es necesario instalar el virtualenv
        con el comando ]{lang="es-ES-u-co-trad"}[**\$ pip install
        virtualenv** ]{lang="es-ES-u-co-trad"}[y posteriormente crear un
        directorio para el proyecto con el comando
        ]{lang="es-ES-u-co-trad"}[**\$ mkdir miproyecto,**
        ]{lang="es-ES-u-co-trad"}[luego debemos dirigirnos al directorio
        con]{lang="es-ES-u-co-trad"}[ **\$ cd miproyecto**
        ]{lang="es-ES-u-co-trad"}[y crear el entorno virtual del
        proyecto con el comando ]{lang="es-ES-u-co-trad"}[**\$
        virtualenv mientornovirtual**]{lang="es-ES-u-co-trad"}[, por
        ultimo se debe activar el entorno virtual con el comando
        ]{lang="es-ES-u-co-trad"}[**\$ .
        mientornovirtual/bin/actívate,** ]{lang="es-ES-u-co-trad"}[ no
        sin recordar que al terminar nuestro desarrollo es recomendable
        desactivar este mismo con el comando
        ]{lang="es-ES-u-co-trad"}[**\$
        deactivate.**]{lang="es-ES-u-co-trad"}

\

2.  [**Flask-CORS:**]{lang="es-ES-u-co-trad"}[ extensión de Flask que
    permite manejar el intercambio de recursos de origen cruzado(CORS),
    su principal característica radica en su filosofía de manejo simple,
    esto debido a que cuando el desarrollador desea habilitar CORS,
    desea habilitarlo para todos los casos de uso en un dominio. Esto
    significa que no hay que perder el tiempo con diferentes
    encabezados, métodos permitidos, entre otros, por lo que este
    paquete expone una extensión Flask que, de una manera
    predeterminada, habilita el soporte de CORS en todas las rutas, para
    todos los orígenes y métodos. Adicionalmente, permite la
    parametrización de todos los encabezados CORS en un nivel por
    recurso. La instalación se ejecuta mediante el comando
    ]{lang="es-ES-u-co-trad"}[**\$ pip install -U flask-cors,**
    ]{lang="es-ES-u-co-trad"}[mientras que para importar a nuestro
    desarrollo es necesario ejecutar en nuestro desarrollo el comando
    ]{lang="es-ES-u-co-trad"}[**from flask\_cors import CORS,
    cross\_origin.**]{lang="es-ES-u-co-trad"}

\

3.  [**Request Flask:** ]{lang="es-ES-u-co-trad"}[utilizado para
    almacenar el contenido que un cliente web envía al servidor del
    aplicativo en cuestión, existen diferentes tipos de request
    dependiendo de la petición que haga el cliente al aplicativo, entre
    los ejemplos se encuentran GET, POST, DELETE, entre otros. Para
    hacer uso del Request dentro de Flask se debe utilizar el comando
    ]{lang="es-ES-u-co-trad"}[**from flask import request**
    ]{lang="es-ES-u-co-trad"}[dentro del
    desarrollo.]{lang="es-ES-u-co-trad"}

\

4.  [**Waitress:** ]{lang="es-ES-u-co-trad"}[los Web Server Gateway
    Interface son las especificaciones que describen cómo se comunica un
    servidor web con una aplicación web y cómo se pueden llegar a
    encadenar diferentes aplicaciones web para procesar una
    solicitud/petición (o request). Python posee una gran variedad de
    servidores WSGI puros, pero Waitress esta destinado a ser útil para
    los autores de marcos web que requieren un amplio soporte de
    plataforma. Por otra parte, ]{lang="es-ES-u-co-trad"}[waitress no
    tiene dependencias, excepto las que viven en la biblioteca estándar
    de Python. La instalación de waitress se ejecuta mediante el comando
    ]{lang="es-ES-u-co-trad"}[**\$ pip install
    waitress.**]{lang="es-ES-u-co-trad"}

\

5.  [**Docker:**]{lang="es-ES-u-co-trad"}[ Es un proyecto de código
    abierto que automatiza el despliegue de aplicaciones dentro de
    contenedores de software, proporcionando una capa adicional de
    abstracción y automatización de virtualización de aplicaciones en
    múltiples sistemas operativos, mediante el uso de características de
    aislamiento de recursos del kernel Linux, tales como cgroups y
    espacios de nombres, permite que \"contenedores\" independientes se
    ejecuten dentro de una sola instancia de Linux, evitando la
    sobrecarga de iniciar y mantener máquinas virtuales.
    ]{lang="es-ES-u-co-trad"}

\

[Luego de esta breve explicación sobre las características de los
recursos a utilizar procedemos a explicar los pasos realizados en el
desarrollo del requerimiento:]{lang="es-ES-u-co-trad"}

\

[Primero se deben construir los servicios para cada una de las
operaciones aritméticas, cada uno de estos se aloja en una carpeta
independiente. Como se puede observar a continuación la estructura del
proyecto contiene una carpeta para cada
servicio.]{lang="es-ES-u-co-trad"}

![](Microservicios_html_aa8e19f4715825ff.png){width="433" height="265"}

[Figura [1]{style="background: #c0c0c0"}: Estructura del
Proyecto]{style="font-style: normal"}

\

Dentro de cada una de las carpetas se tiene el servicio de cada
operación aritmética, el archivo docker y los requerimientos necesarios.

\

![](Microservicios_html_2648e5c0984e4a65.png){width="460" height="130"}

[Figura [2]{style="background: #c0c0c0"}: Estructura de los
servicios]{style="font-style: normal"}

Cada uno de los servicios debe importar las herramientas necesarias para
su correcto funcionamiento en el desarrollo, primero se debe importar
Flask, render\_template, request, jsonify, posteriormente flask\_cors y
waitress y por último json, requests y traceback.

\

![](Microservicios_html_45c5dc87300aeb6b.png){width="578" height="153"}

[Figura [3]{style="background: #c0c0c0"}: Importación de las
herramientas]{style="font-style: normal"}

A continuación, se muestra la lógica utilizada en el llamado de los
servicios y adicionalmente la definición del host que alojara la
aplicación principal del desarrollo.

![](Microservicios_html_33bffbdfce645032.png){width="659" height="391"}

[Figura [4]{style="background: #c0c0c0"}: Lógica para llamar a los
servicios]{style="font-style: normal"}

\

![](Microservicios_html_2b8e2de294f50d21.png){width="551" height="83"}

[Figura [5]{style="background: #c0c0c0"}: Definición del Host
(waitress)]{style="font-style: normal"}

Posteriormente se define la lógica de cada uno de los servicios, en la
siguiente figura se observa la lógica del servicio de suma desarrollado.

![](Microservicios_html_38db6d1429a543f8.png){width="525" height="521"}

[Figura [6]{style="background: #c0c0c0"}: Lógica de los servicios
(suma)]{style="font-style: normal"}

\
Luego de desarrollar cada uno de los servicios es necesario crear los
contenedores de los mismos, por esta razón, en todos los servicios es
necesario crear un archivo Dockerfile que se encarga de crear un orden
de las tareas necesarias para que los servicios que se van a ejecutar
operen de manera correcta sin necesidad de hacer instalaciones o pasos
intermedios.

![](Microservicios_html_c35b33201faab3cc.png){width="396" height="315"}

[Figura [7]{style="background: #c0c0c0"}: Dockerfile
(app)]{style="font-style: normal"}

![](Microservicios_html_c54d47fe2abfa48b.png){width="406" height="312"}

[Figura [8]{style="background: #c0c0c0"}: Dockerfile Servicios
(suma)]{style="font-style: normal"}

\

[Después de crear cada uno de los archivos Dockerfile para cada servicio
se procede a crear el archivo "docker-compose.yml", dicho archivo es el
encargado de realizar de manera automática la creación de las imágenes y
dejar en contenedores los servicios listos para su despliegue, en este
archivo especificamos los puertos y los nombres de los contenedores para
que se puedan comunicar entre ellos.]{lang="es-ES-u-co-trad"}

![](Microservicios_html_7c6b8c1de2f63c33.png){width="419" height="853"}

[Figura [9]{style="background: #c0c0c0"}:
docker-compose.yml]{style="font-style: normal"}

Posteriormente se valida el correcto funcionamiento de la herramienta
Docker Desktop.

![](Microservicios_html_830a3560dbb30802.png){width="531" height="182"}

[[Figura
]{style="font-style: normal"}]{lang="en-US"}[[10]{style="background: #c0c0c0"}]{style="font-style: normal"}[[:
Validación Docker Desktop is
Running]{style="font-style: normal"}]{lang="en-US"}

[Después de ejecutar la instrucción "docker-compose up" podemos ver como
los contenedores son desplegados.]{lang="es-ES-u-co-trad"}

\

![](Microservicios_html_1b14e6898028e76f.png){width="624" height="143"}

[Figura [11]{style="background: #c0c0c0"}: Servicios
Iniciados]{style="font-style: normal"}*\
*\
\

**Enlaces de interés:**

\

\[1\] <https://www.python.org/downloads/>

\

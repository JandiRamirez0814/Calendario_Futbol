# Funcionales

##Instalar entorno virtual:
Lo primero que debe hacerse es  instalar **virtualenv** si aún no esta instalado, se abre una terminal y se escribe el siguiente comando:
> pip install virtualenv

Después se ejecutan las siguientes lineas en terminal que crearán el entorno virtual, y luego lo activan:
> - virtualenv nombre_del_entorno
> - cd  nombre_del_entorno/Scripts
> - .\activate

Es importante tener habilitada la ejecución se Scripts en el sistema ya que de lo contrario se generarán problemas a la hora de utilizar el entorno virtual,  [aquí](https://www.youtube.com/watch?v=9HYQsCjKAmg&pp=ygUxaGFiaWxpdGFyIGVqZWN1Y2lvbiBkZSBzY3JpcHRzIHZpc3VhbCBzdHVkaW8gY29kZQ%3D%3D "aquí") hay un tutorial que puede ayudar con esta situación.

Una vez el entorno virtual esta activo, se instalarán las librerías mediante el uso del archivo *requeriments.txt*, primero se ira a la carpeta raiz.
> - cd..
> - cd..
> - pip install -r requirements.txt

Una vez instaladas nuestras librerías podemos empezar a ejecutar nuestros archivos.

##Ejecución
###Funcionalidades
En esta carpeta podrás encontrar cuatro archivos eejecutables:
- calendario.py
- sol_ingenua.py
- tiempo.py
- espacio.py

####calendario.py
Puedes ejecutar estos archivos escribiendo en la terminal si te encuentras en la carpeta raiz los siguientes comandos:

> - python Funcionales/calendario.py

Este comando iniciara una interfaz de este aspecto: 
[![1](https://co.pinterest.com/pin/1003458360712297885/ "1")](https://co.pinterest.com/pin/1003458360712297885/ "1")
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
Cuando se haga click en el boton **Cargar Archivo** se abrira una interfaz como esta: [![2](https://co.pinterest.com/pin/1003458360712288295/ "2")](https://co.pinterest.com/pin/1003458360712288295/ "2")
este programa recibe archivos **.txt** cuyo formato es de esta forma:

- Primera linea: Cantidad de equipos. (int)
- Segunda linea: cantidad minima de  partidos, local y visitante (int)
- Tercera linea: cantidad maxima de partidos, local y visitante (int)
- Resto de lineas: Una matriz de distancias para los equipos cuya diagonal esta compuesta de 0's.

Cuando se selecciones el archivo la interfaz mostrara los resultados en este formato:
- [![3](https://co.pinterest.com/pin/1003458360712288287/ "3")](https://co.pinterest.com/pin/1003458360712288287/ "3")
- [![5](https://co.pinterest.com/pin/1003458360712288277/ "5")](https://co.pinterest.com/pin/1003458360712288277/ "5")

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

Se puede dar click nuevamente el boton y seleccionar otro archivo y la insterfaz cambiará.

####sol_ingenua.py
El proceso es esencialmente el mismo, ya que ambos comparten los mismo mecanismos de interfaz y lectura de archivos.

> - python Funcionales/sol_ingenua.py

Este comando iniciara una interfaz de este aspecto: 
[![1](https://co.pinterest.com/pin/1003458360712297885/ "1")](https://co.pinterest.com/pin/1003458360712297885/ "1")
![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
Cuando se haga click en el boton **Cargar Archivo** se abrira una interfaz como esta: [![2](https://co.pinterest.com/pin/1003458360712288295/ "2")](https://co.pinterest.com/pin/1003458360712288295/ "2")
este programa recibe archivos **.txt** cuyo formato es de esta forma:

- Primera linea: Cantidad de equipos. (int)
- Segunda linea: cantidad minima de  partidos, local y visitante (int)
- Tercera linea: cantidad maxima de partidos, local y visitante (int)
- Resto de lineas: Una matriz de distancias para los equipos cuya diagonal esta compuesta de 0's.

Cuando se selecciones el archivo la interfaz mostrara los resultados en este formato:
- [![3](https://co.pinterest.com/pin/1003458360712288287/ "3")](https://co.pinterest.com/pin/1003458360712288287/ "3")
- [![5](https://co.pinterest.com/pin/1003458360712288277/ "5")](https://co.pinterest.com/pin/1003458360712288277/ "5")

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)

Se puede dar click nuevamente el boton y seleccionar otro archivo y la insterfaz cambiará.

####tiempo.py
Esta es una prueba que toma el tiempo promedio que le demora al algoritmo calendario y al algoritmo sol_ingenua generar sus soluciones realizando 1000 pruebas para diferentes cantidades de equipos, imprimiendo al final dos tablas donde se muestran los resultados.
> - python Funcionales/tiempo.py

El resultado se mostrará en terminal de esta forma: [![6](https://co.pinterest.com/pin/1003458360712297892/ "6")](https://co.pinterest.com/pin/1003458360712297892/ "6")

Ejecutando el mismo comando se empezará otra prueba.

####espacio.py
Esta prueba consiste en tomar el espacio que se requiere cada vez que se ejecuta el algoritmo calendario y el algoritmo sol_ingenua, siendo que los resultados pueden variar por multiples factores como:
- Dispositivo
- Si la función utiliza recursión, la profundidad de la pila puede afectar el uso de memoria.
- Los bucles y las estructuras de control pueden afectar la eficiencia del uso de memoria. La creación y eliminación de variables dentro de bucles también puede influir.
- La frecuencia de la recolección de basura puede afectar la liberación de memoria.

Una vez esto dicho, se puede ejecutar el siguiente comando:
> - python Funcionales/espacio.py

Luego se mostrará en la interfaz los resultados de esta manera: [![7](https://co.pinterest.com/pin/1003458360712298250 "7")](https://co.pinterest.com/pin/1003458360712298250 "7")
Ejecutando el mismo comando se llamara de nuevo a una nueva prueba.

###Documentación
Se puede acceder a la documentación del proyectos introduciendo los siguientes comandos, teniendo como base que estamos en la carpeta raiz:

> - cd docs/build/html
> - start index.html

Este comando abrirá la siguiente interfaz a través de la que se puede navegar toda la documentación del proyecto.

Se veria de esta forma: [![8](https://co.pinterest.com/pin/1003458360712298360 "8")](https://co.pinterest.com/pin/1003458360712298360 "8")

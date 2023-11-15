# Ayudantía - Ejemplos de Backend y pruebas de endpoints

**INF3240 - Ingeniería Web**<br />
**Escuela de Ingeniería Informática**<br />
**Pontificia Universidad Católica de Valparaíso**

* * *

<!-- omit in toc -->
## Índice
<!--  -->
- [Información](#información)
  - [Datos ayudantía](#datos-ayudantía)
  - [Tecnologías utilizadas](#tecnologías-utilizadas)
  - [Archivos](#archivos)
- [Pasos iniciales](#pasos-iniciales)
  - [Proyecto de Express.js](#proyecto-de-expressjs)
  - [Proyecto de Flask](#proyecto-de-flask)
- [Actividades](#actividades)
  - [Pruebas de endpoints](#pruebas-de-endpoints)
  - [Agregar ruta](#agregar-ruta)

* * *

## Información

### Datos ayudantía

- **Número:** 11
- **Semana:** 13 al 17 de noviembre de 2023
- **Temática:** Ejemplos de Backend y pruebas de endpoints

### Tecnologías utilizadas

- [![ts-badge]][ts-web]
- [![node-badge]][node-web]
- [![expressjs-badge]][expressjs-web]
- [![python-badge]][python-web]
- [![flask-badge]][flask-web]
- [![sqlite-badge]][sqlite-web]
- [![dotenv-badge]][dotenv-web]
- [![jwt-badge]][jwt-web]

### Archivos

| Título                   | Formato           | Archivo (link)                          |
| ------------------------ | ----------------- | --------------------------------------- |
| ay11-backend-flask | `carpeta zip`     | Descarga en Aula Virtual                |
| ay11-backend-express      | `carpeta zip`     | Descarga en Aula Virtual                |
| ay-inf3240-ejemplos-backend       | `repositorio git` | [Ir al repo de GitHub][repo-github-web] |

* * *

## Pasos iniciales

### Proyecto de Express.js

1. Descargar los archivos `ay11-backend-express.zip` de la ayudantía desde Aula Virtual, o clonar desde el repositorio de Github [en este link][repo-github-web].
2. Si descargaste los zip, descomprimir el archivo.
3. Abrir una ventana en Visual Studio Code, y abrir la carpeta `ay11-express` en Visual Studio Code.
4. Presionar las teclas <kbd>Ctrl</kbd> + <kbd>ñ</kbd> para abrir la terminal integrada de Visual Studio Code (también puede acceder presionando <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> y escribir la palabra `terminal`).
5. Instalar las dependencias de NPM con el comando:

    ```bash
    npm install
    ```

    o

    ```bash
    yarn install
    ```

6. Ejecutar cada proyecto con el comando:

    ```bash
    npm run start
    ```

    o

    ```bash
    yarn start
    ```

### Proyecto de Flask

1. Descargar los archivos `ay11-backend-flask.zip` de la ayudantía desde Aula Virtual, o clonar desde el repositorio de Github [en este link][repo-github-web].
2. Si descargaste los zip, descomprimir el archivo.
3. Abrir una ventana en Visual Studio Code, y abrir la carpeta `ay11-flask` en Visual Studio Code.
4. Presionar las teclas <kbd>Ctrl</kbd> + <kbd>ñ</kbd> para abrir la terminal integrada de Visual Studio Code (también puede acceder presionando <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> y escribir la palabra `terminal`).
5. Primero revisar la versión de Python con el comando `python --version`. Si la versión es menor a 3.10, actualizar/instalar Python a una versión igual o superior a 3.10.
6. Crear un entorno virtual de Python con el comando:

    ```bash
    python -m venv venv
    ```

7. Iniciar el entorno virtual de Python con el comando:

    ```bash
    .\venv\Scripts\activate
    ```

    Desde Windows, y desde macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

8. Instalar las dependencias de Python con el comando:

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

9. Ejecutar el proyecto con el comando:

    ```bash
    python app.py
    ```

10. Para salir del entorno virtual de Python, ejecutar el comando:

    ```bash
    deactivate
    ```

* * *

## Actividades

Para ambas actividades, la idea es elegir entre el proyecto de Express.js o el proyecto de Flask, y realizar las siguientes actividades.

### Pruebas de endpoints

Esta será una actividad práctica durante la sesión de ayudantía, en donde abordaremos como probar los endpoints de nuestras APIs usando RapidAPI (aplicable los principios también para otros softwares, como Postman e Insomnia). Las instrucciones se entregarán durante la ayudantía.

### Agregar ruta

Con el proyecto escogido, agregar una nueva ruta, de su elección personal, y que gestione seleccion, insersión, actualización y eliminación de la misma, utilizando el ORM del proyecto en particular (TypeORM para el de Express, y SQLAlchemy para el de Flask). El requerimiento es:

- La ruta que obtiene todos los objetos, debe ser pública.
- La ruta que obtiene un objeto en particular, debe ser solo accesible por usuarios autenticados.
- La ruta que inserta un objeto, debe ser solo accesible por usuarios autenticados.
- La ruta que actualiza un objeto, debe ser solo accesible por usuarios autenticados.
- La ruta que elimina un objeto, debe ser solo accesible por usuarios autenticados.

* * *

[node-badge]: https://img.shields.io/badge/Node.js-339933?logo=node.js&logoColor=fff&style=flat
[node-web]: https://nodejs.org/es/
[python-badge]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat
[python-web]: https://www.python.org/
[flask-badge]: https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=fff&style=flat
[flask-web]: https://flask.palletsprojects.com/en/2.0.x/
[ts-badge]: https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=fff&style=flat
[ts-web]: https://www.typescriptlang.org/
[expressjs-badge]: https://img.shields.io/badge/Express.js-000000?logo=express&logoColor=fff&style=flat
[expressjs-web]: https://expressjs.com/
[sqlite-badge]: https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=flat
[sqlite-web]: https://www.sqlite.org/index.html
[dotenv-badge]: https://img.shields.io/badge/dotenv-000000?logo=dotenv&logoColor=fff&style=flat
[dotenv-web]: https://www.npmjs.com/package/dotenv
[jwt-badge]: https://img.shields.io/badge/JSON%20Web%20Tokens-000?logo=jsonwebtokens&logoColor=fff&style=flat
[jwt-web]: https://jwt.io/
[repo-github-web]: https://github.com/sebaignacioo/ay-inf3240-ejemplos-backend

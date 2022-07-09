# bookgym-bot


<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


Este proyecto representa un bot para la reserba de sessiones de entrenamiento en la aplicación **aimharder.com**


Características :

* Proporciona una API Flask para operaciones de gestión mediante HTTP
  * Funcionalidad de "is alive"
* Proporciona las funcionalidades de reserva de sesiones de entrenamiento
  * Registro de usuario con username como identificador
  * 
* Logging
* Despliegue en Contenedor
  * Contenedor de Python para uso en ordenadores
  * Contenedor de Python para uso en raspberrys
* Proporciona un planificador para levantar el porgrama cada ciertas horas

## Stack Tecnológico

### General

* [Python](https://www.python.org/) 3.9.x



### Dependencias proyectos de arquitectura

N/A


### Dependencias de terceros

**Desarrollo**

* **Flask** : Framework ligero (microframework) para el desarrollo de aplicaciones web
  * [Pypi](https://pypi.org/project/Flask/)
  * [Repositorio](https://github.com/pallets/flask/)
  * [Documentacion](https://flask.palletsprojects.com/en/2.1.x/)
  * Incluye las siguientes dependencias :
    * click: package for creating command-line interfaces (CLI)
    itsdangerous: cryptographically sign data
    Jinja2: templating engine
    MarkupSafe: escapes characters so text is safe to use in HTML and XML
    Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server


**Testing / QA**

* **pipdeptree** : Utilidad de línea de domandos para mostrar el arbol de dependencias
  * [Pypi](https://pypi.org/project/pipdeptree/)
  * [Repositorio](https://github.com/naiquevin/pipdeptree)
  * [Documentacion](https://pypi.org/project/pipdeptree/)
* **graphviz** : Interfaz Graphviz
  * [Pypi](https://pypi.org/search/?q=graphviz)
  * [Repositorio](https://github.com/xflr6/graphviz)
  * [Documentacion](https://github.com/xflr6/graphviz)
* **black** : Formateador de código con pocas opciones de configuración lo que proporciona un estilo consistente para que apliquen todos los equipos de desarrollo
  * [Pypi](https://pypi.org/project/black/)
  * [Repositorio](https://github.com/psf/black)
  * [Documentacion](https://black.readthedocs.io/en/stable/)
* **pylint** : Framework de chequeo sobre el código. Se encarga de : errores de programación, codificación estandar, olores de código, etc.
  * [Pypi](https://pypi.org/project/pylint/)
  * [Repositorio](https://github.com/PyCQA/pylint/)
  * [Documentacion](https://pylint.pycqa.org/en/latest/)
* **pytest** : Framework para testing unitario (con más de 850+ plugins externos)
  * [Pypi](https://pypi.org/project/pytest/)
  * [Repositorio](https://github.com/pytest-dev/pytest)
  * [Documentacion](https://docs.pytest.org/en/latest/)
* **pytest-flask** : Extensión de pytest que proporciona un conjunto de características para facilitar el testing sobre Flask
  * [Pypi](https://pypi.org/project/pytest-flask/)
  * [Repositorio](https://github.com/pytest-dev/pytest-flask)
  * [Documentacion](https://pytest-flask.readthedocs.io/en/latest/)
* **pytest-black** : Extensión de pytest que proporciona un el chequeo del formateo sobre el testing con black
  * [Pypi](https://pypi.org/project/pytest-black/)
  * [Repositorio](https://github.com/shopkeep/pytest-black)
  * [Documentacion](https://github.com/shopkeep/pytest-black)
* **pytest-clarity** : Extensión de pytest que proporciona características de ayuda en la salida por consola al hacer diff en asserts, etc.
  * [Pypi](https://pypi.org/project/pytest-clarity/)
  * [Repositorio](https://github.com/darrenburns/pytest-clarity)
  * [Documentacion](https://github.com/darrenburns/pytest-clarity)
* **pytest-xdist** : Extensión de pytest que proporciona características de ejecución de test de forma distribuida
  * [Pypi](https://pypi.org/project/pytest-xdist/)
  * [Repositorio](https://github.com/pytest-dev/pytest-xdist)
  * [Documentacion](https://pytest-xdist.readthedocs.io/en/latest/)
* **pytest-cov** : Extensión de pytest que proporciona los datos de cobertura sobre los tests
  * [Pypi](https://pypi.org/project/pytest-cov/)
  * [Repositorio](https://github.com/pytest-dev/pytest-cov)
  * [Documentacion](https://pytest-cov.readthedocs.io/en/latest/)
* **pytest-flake8** : Extensión de pytest que proporciona característica de chequeo sobre FLAKE 8
  * [Pypi](https://pypi.org/project/pytest-flake8/)
  * [Repositorio](https://github.com/tholo/pytest-flake8)
  * [Documentacion](https://pypi.org/project/pytest-flake8/)
* **pytest-mock** : Extensión de pytest que proporciona características de mocking
  * [Pypi](https://pypi.org/project/pytest-mock/)
  * [Repositorio](https://github.com/pytest-dev/pytest-mock/)
  * [Documentacion](https://pypi.org/project/pytest-mock/)
* **pytest-cases** : Extensión de pytest que proporciona la separación entre codigo de test y los casos de test
  * [Pypi](https://pypi.org/project/pytest-cases/)
  * [Repositorio](https://github.com/smarie/python-pytest-cases)
  * [Documentacion](https://smarie.github.io/python-pytest-cases/)
* **pytest-asyncio** : Extensión de pytest que proporciona características de asincronía sobre los test
  * [Pypi](https://pypi.org/project/pytest-asyncio/)
  * [Repositorio](https://github.com/pytest-dev/pytest-asyncio)
  * [Documentacion](https://github.com/pytest-dev/pytest-asyncio)
* **autoflake** : Framework que permite hacer ciertos cambios sobre el código (imports , variables, ...)
  * [Pypi](https://pypi.org/project/autoflake/)
  * [Repositorio](https://github.com/PyCQA/autoflake)
  * [Documentacion](https://pypi.org/project/autoflake/)
* **freezegun** : Framework que facilita trabajar con tiempo en los test
  * [Pypi](https://pypi.org/project/freezegun/)
  * [Repositorio](https://github.com/spulec/freezegun)
  * [Documentacion](https://github.com/spulec/freezegun)
* **bandit** : Framework de analisis de seguridad orientado al analisis estático
  * [Pypi](https://pypi.org/project/bandit/)
  * [Repositorio](https://github.com/PyCQA/bandit)
  * [Documentacion](https://bandit.readthedocs.io/en/latest/)
* **safety** : Framework de analisis de seguridad orientado a las vulnerabilidades y licencias
  * [Pypi](https://pypi.org/project/safety/)
  * [Repositorio](https://github.com/pyupio/safety)
  * [Documentacion](https://pyup.io/safety/)
* **requests-mock** : Framework que facilita mockear la librería "request" 
  * [Pypi](https://pypi.org/project/requests-mock/)
  * [Repositorio](https://github.com/jamielennox/requests-mock)
  * [Documentacion](https://requests-mock.readthedocs.io/en/latest/)






## Pre-Requisitos

* Python 3 (>=3.9) 
* Docker instalado (19+)





## Instalación

Pasos a seguir

* Arrancar un terminal
* Localizar el PATH de instalación (el lugar donde se encuentra el proyecto)


### Instalación con Entorno Virtual local

1. Verificar que el fichero "Makefile" esta disponible

2. Ejecutar el siguiente comando

```bash
make init-venv
```




## Testing

1. Verificar que el fichero "Makefile" esta disponible

2. Ejecutar el siguiente comando

```bash
make test
```



# Despliegue


En Construcción




## Swagger

No Aplica




## Dockerize

1. Verificar que el fichero "Makefile" esta disponible

2. Ejecutar el siguiente comando

```bash
make docker-build
```

3. Verificar que existe la imagen creada

4. Ejecutar el siguiente comando

Create a Docker container

```bash
make docker-run
```

5. Probar la siguiente URL desde el navegador

```bash
http://localhost:5000/manager/isalive
```


## Uso




## Versionada

**Nota :** [SemVer](http://semver.org/) es utilizado por el versionado

Para ver las versiones disponibles ver los tags del repositorio





## Autores

* **Víctor Madrid**


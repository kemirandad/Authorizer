# Authorizer

_Validaciones de operaciones realizadas con una cuenta bancaria a través de entradas en formato JSON, manipulado por consola de comandos_

## Comenzando 🚀

_1. Se utilizo la libreria JSON incluida en el paquete por default de Python._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Pyhton v. 3.9_
_Python for VS Code v. 0.2.3_
_Librerias json y datetime_

```
import json
from datetime import datetime
```

### Instalación 🔧

_Clona este proyecto_

```
git clone https://github.com/kemirandad/Authorizer.git
```

_Ejecutar desde la terminal de comandos_

```
python3.9 main.py
```

_Ejemplo inputs y outputs_
```
input
{ "transaction": { "merchant": "Burger King", "amount": 20, "time": "2019-02-13T10:00:00.000Z" } }
output
{ "account": { "activeCard": true, "availableLimit": 80 }, "violations": [] }
```
```
input
{ "transaction": { "merchant": "Habbib's", "amount": 90, "time": "2019-02-13T11:00:00.000Z" } }
output
{ "account": { "activeCard": true, "availableLimit": 80 }, "violations": [ "insufficient-limit" ] }
```
## Ejecutando las pruebas ⚙️

_Prueba unitaria para el método change_status del módulo create_account_
```
import unittest
```
_Para ejecutar la prueba_
```
cd Nu
python3.9 ./Test/status_change_test.py
```

## Construido con 🛠️

* [Python](https://www.python.org/doc/) - El lenguaje usado
* [PIP](https://pypi.org/project/pip/) - Manejador de dependencias


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en mi repo [Wiki](https://github.com/kemirandad/Authorizer)

## Autor(es) ✒️

* **Kenny Miranda** - *Trabajo Inicial* - [kemirandad](https://github.com/kemirandad)


## Licencia 📄

Este proyecto está bajo la Licencia (GNU) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

---
⌨️ por [kemirandad](https://github.com/kemirandad) 😊
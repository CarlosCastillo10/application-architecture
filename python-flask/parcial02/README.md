# Segunda evaluación parcial del primer bimestre
---

### Explicación del funcionamiento
**Video:** [https://youtu.be/Xkvc2jEArm0](https://youtu.be/Xkvc2jEArm0)

### Instalación ([Recomendable hacerlo en un entorno virtual](https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace))
* Ejecutar ```pip install --upgrade pip```
* Ejecutar ```pip install -r requirements.txt```
* Ejecutar en el motor de base de datos MySQL el archivo: [parcial02-script.sql](https://github.com/CarlosCastillo10/application-architecture/blob/main/python-flask/parcial02/parcial02-script.sql)
<p align="center">
<img src='https://github.com/CarlosCastillo10/application-architecture/blob/main/python-flask/parcial02/utpl-sqlmodel.png' alt='DB Model' title='Relational Model' height='400'>
</p>

---
### Ejecución
* Ubicarse en la raíz del repositorio.
* Activar la configuración del servidor:
  * Linux o Mac:  ``` . configurarion.sh ```
  * Windows: ``` configuration.bat ```
* Ejecutar la aplicación ```flask run```

---
### Uso
* La aplicación se estará ejecutando en: [http://localhost:5000/](http://localhost:8082/)
---

### Funcionalidades
**Importante:** Realizar las pruebas desde un cliente como [postman](https://web.postman.co/) que permita configurar headers ya que la aplicación soporta solo
aquellos clientes que acepten JSON.

| Método | Ruta                           | Acción                                              |  
|--------|--------------------------------|-----------------------------------------------------| 
| `GET`  | `/knowledge-areas`             | Devuelve todas las areas de conocimiento            |
| `GET`  | `/knowledge-area/:id`          | Devuelve el area de conocimiento segun el "id"      |
| `GET`  | `/knowledge-area/:id/faculties`| Devuelve las facultades de una area de conocimiento |
| `GET`  | `/faculty/:id`                 | Devuelve la facultad segun el "id"                  |
| `GET`  | `/faculty/:id/departments`     | Devuelve los departamentos de una facultad          |
| `GET`  | `/department/:id`              | Devuelve un departamento segun el "id"              |
| `GET`  | `/department/:id/degrees`      | Devuelve las titulaciones de un departamento        |
| `GET`  | `/degree/:id`                  | Devuelve una titulación segun el "id"               |
| `GET`  | `/degree/:id/courses`          | Devuelve las asignturas de una titulación           |
| `GET`  | `/course/:id`                  | Devuelve una asignatura segun el "id"               |
| `GET`  | `/course/:id/students`         | Devuelve los estudiantes de una asignatura          |
| `GET`  | `/student/:id`                 | Devuelve un estudiante segun el "id"                |


# API RESTFUL
---

### Instalación ([Recomendable hacerlo en un entorno virtual](https://medium.com/@m.monroyc22/configurar-entorno-virtual-python-a860e820aace))
* Ejecutar ```pip install --upgrade pip```
* Ejecutar ```pip install -r requirements.txt```

---
### Ejecución
* Ubicarse en la raíz del repositorio.
* Activar la configuración del servidor:
  * Linux:  ``` . configurarion.sh ```
  * Windows: ``` configuration.bat ```
* Ejecutar la aplicación ```flask run```

---
### Uso
* La aplicación se estará ejecutando en: [http://localhost:5000/](http://localhost:8082/)
---

### Funcionalidades
**Importante:** Realizar las pruebas desde un cliente como [postman](https://web.postman.co/) que permita configurar headers ya que la aplicación soporta solo
aquellos clientes que acepten JSON.

| Método | Ruta                 |   Acción                                                                     |  
|------- | -------------------- | ---------------------------------------------------------------------------- | 
| `GET`    | `/students`        | Devuelve todos los estudiantes                                               |
| `GET`    | `/student/:pos`    | Devuelve al estudiante ubicado en la posición "pos"                          |
| `GET`    | `/students/filter` | Devuelve los estudiantes que cumplen con un filtro **(name, lastname, age)** |
| `POST`   | `/student`         | Agrega un estudiante a la lista                                              |
| `PUT`    | `/students/:pos`   | Actualiza al estudiante de la posición "pos"                                 |
| `DELETE` | `/student/:pos`    | Elimina al estudiante de la posición "pos"                                   |

**Nota:** Siempre se agrega o actualiza todos los atributos de un estudiante.

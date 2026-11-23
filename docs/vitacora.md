# Bitácora G05 · Gimnasio «Fuerza Austral»

Equipo: Manuel Montecinos, Claudio Cáceres y Giovanni Ávila.
Repositorio: `evaluacion_finall_back_end_Montecinos_caceres_avila`.

---

## Semana 1 · Diseño, base de datos y conexión

### Manuel Montecinos

**Qué hice**
Dejé armado el repositorio con la estructura `backEnd/`, `frontend/` y `docs/`, el `.gitignore`, el `.env.example`, el `requirements.txt` y el `README.md`. Después diseñé el modelo entidad-relación de las cinco tablas (planes, socios, instructores, clases e inscripciones) y escribí el diccionario de datos. Con eso escribí los dos scripts de Oracle, los ejecuté en mi esquema de FreeSQL y comprobé con `user_tables` que las cinco tablas quedaron creadas y con datos.

En la parte de Django creé el entorno virtual, instalé las dependencias (Django 5.2.19), creé el proyecto `gimnasio_project` y la aplicación `gimnasio`, y dejé las carpetas de las cuatro capas. Configuré `settings.py` con dos bases de datos (SQLite para las tablas internas de Django y Oracle para el negocio) y creé el router. Probé la conexión con `python manage.py check --database negocio`, que respondió sin errores, y usé `inspectdb` para ver cómo Django lee mis tablas.

**Archivos**
- `docs/g05_modelo_entidad_relacion.png`
- `docs/diccionario_datos.md`
- `docs/captura_user_tables.png`
- `backEnd/sql/01_crear_tablas.sql`
- `backEnd/sql/02_datos_ejemplo.sql`
- `backEnd/gimnasio_project/settings.py`
- `backEnd/gimnasio_project/routers.py`
- `backEnd/.env.example`, `backEnd/requirements.txt`, `.gitignore`, `README.md`

**Problemas y cómo los resolví**
- Mi esquema de FreeSQL todavía tenía las tablas del ejemplo del manual (clientes, productos, ventas y otras). Las borré con `DROP TABLE` antes de crear las del proyecto, para que `user_tables` mostrara solo las cinco nuestras.
- La imagen del modelo no se abría en VS Code porque la había pegado en vez de copiar el archivo. Descargué la imagen, la moví desde el explorador de archivos a `docs/` y ahí cargó bien.
- Mi terminal era `cmd` y el comando de activación del manual (`Activate.ps1`) es de PowerShell, por lo que Windows abrió un cuadro para elegir programa. Usé `entorno\Scripts\activate.bat` y funcionó.

**Uso de IA**
Usé Claude para analizar el enunciado y el manual, para proponer las columnas de las tablas y para redactar borradores del diccionario, de los scripts SQL y de los datos de ejemplo. Ejecuté los scripts en mi esquema, revisé el resultado en FreeSQL y probé la conexión yo mismo.

**Próxima semana**
Escribir las capas hexagonales: entidades, puertos, excepciones, casos de uso de las maestras, modelos y repositorios.

### Claudio Cáceres

(Completar: qué hice, archivos, problemas y cómo los resolví, uso de IA y qué haré la próxima semana. Ejecuté los scripts SQL en mi propio esquema de FreeSQL.)

### Giovanni Ávila

(Completar: qué hice, archivos, problemas y cómo los resolví, uso de IA y qué haré la próxima semana. Ejecuté los scripts SQL en mi propio esquema de FreeSQL.)

---

## Semana 2 · Capas hexagonales de las entidades maestras

### Manuel Montecinos · instructores

**Qué hice**
Me encargué de la entidad `instructores` y de lo compartido. Escribí la entidad `Instructor` y el puerto `InstructorRepository`. Escribí también las excepciones de negocio de todo el proyecto, agrupadas en tres familias (no encontrado, duplicado y regla de negocio), incluidas las de las reglas R1, R2 y R3 y la de cambio de estado inválido. Armé los casos de uso CRUD de instructores: listar, obtener, crear, actualizar y eliminar. Al crear y actualizar se controlan los duplicados de RUT, email y usuario, y al eliminar se protege el borrado cuando el instructor tiene clases. En infraestructura creé el modelo `InstructorModel` con `managed = False` y el repositorio `DjangoInstructorRepository`, además de los `__init__.py` que agrupan cada carpeta.

**Archivos**
- `backEnd/gimnasio/domain/entities/instructor.py`
- `backEnd/gimnasio/domain/repositories/instructor_repository.py`
- `backEnd/gimnasio/application/exceptions.py`
- `backEnd/gimnasio/application/use_cases/instructor_use_cases.py`
- `backEnd/gimnasio/infrastructure/models/instructor.py`
- `backEnd/gimnasio/infrastructure/repositories/instructor_repository.py`
- Los cinco `__init__.py` de `domain/entities`, `domain/repositories`, `application/use_cases`, `infrastructure/models` e `infrastructure/repositories`

**Problemas y cómo los resolví**
Al copiar la carpeta `gimnasio` sobre la existente, Windows la reemplazó completa y GitHub Desktop mostró 16 archivos como eliminados: eran los archivos de Claudio, que yo ya había traído con el Pull. Para no subir esos borrados desmarqué los archivos eliminados, hice el commit solo con los 11 archivos míos y después descarté los cambios de los eliminados para recuperar los archivos de Claudio.

**Uso de IA**
Usé Claude para generar el código base de las capas siguiendo el patrón del manual adaptado a nuestro problema, y para repartir los archivos entre Claudio y yo. Revisé mis archivos, los subí con mi cuenta y probé los casos de uso de instructores desde `python manage.py shell` contra mi esquema de Oracle.

**Próxima semana**
Casos de uso de clases e inscripciones con las reglas R1, R2 y R3 y las transiciones de estado, panel de administración, grupos y permisos, y login con cookie HttpOnly y CSRF.

### Claudio Cáceres · planes, socios, clases e inscripciones

**Qué hice**
Me encargué de las entidades `planes`, `socios`, `clases` e `inscripciones`. Escribí las entidades de dominio y los puertos de las cuatro. Armé los casos de uso CRUD de planes y socios: el nombre del plan es único, el RUT y el email del socio son únicos, el plan de un socio debe existir, y no se puede eliminar un plan con socios ni un socio con inscripciones. En infraestructura escribí los modelos de las cuatro entidades con `managed = False` (con la columna virtual `precio_anual` y la clave primaria compuesta de `inscripciones`) y los repositorios de planes y socios.

**Archivos**
- `backEnd/gimnasio/domain/entities/`: `plan.py`, `socio.py`, `clase.py`, `inscripcion.py`
- `backEnd/gimnasio/domain/repositories/`: `plan_repository.py`, `socio_repository.py`, `clase_repository.py`, `inscripcion_repository.py`
- `backEnd/gimnasio/application/use_cases/`: `plan_use_cases.py`, `socio_use_cases.py`
- `backEnd/gimnasio/infrastructure/models/`: `plan.py`, `socio.py`, `clase.py`, `inscripcion.py`
- `backEnd/gimnasio/infrastructure/repositories/`: `plan_repository.py`, `socio_repository.py`

**Problemas y cómo los resolví**
(Completar.)

**Uso de IA**
(Completar.)

**Próxima semana**
(Completar.)
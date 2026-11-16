# G05 · Gimnasio «Fuerza Austral»

Proyecto final de Back End (INACAP 2026): API hexagonal con Django, Oracle y React.

## Integrantes

| Integrante 

| Manuel Montecinos 
| Claudio Caceres
giovani avila
## El problema

El gimnasio ofrece clases grupales con cupo limitado. Los socios con membresía vigente se inscriben en ellas.

**Entidades:** planes, socios, instructores, clases, inscripciones.

**Estados de la clase:** programada → realizada · programada → suspendida

**Reglas de negocio**
- **R1** No se inscribe en una clase llena ni en una que no esté `programada`.
- **R2** Solo socios con membresía vigente (`fecha_vencimiento` ≥ fecha de la clase).
- **R3** Un socio no supera las clases por semana de su plan.

**Roles:** `administrador` (todo) · `instructor` (marca asistencia de sus clases; no edita socios ni planes).

**Reporte:** ocupación (%) de cada clase de la semana y socios con membresía por vencer en 7 días.

## Tecnologías

Python 3.12 o superior · Django 5.2 LTS · Django REST Framework · Oracle 26ai (FreeSQL) · React + Vite

## Estructura del repositorio

```
backEnd/
├── manage.py
├── requirements.txt
├── .env.example
├── sql/                  scripts de Oracle
├── gimnasio_project/     configuración del proyecto (settings, routers)
└── gimnasio/             aplicación, organizada en capas
    ├── domain/
    ├── application/
    ├── infrastructure/
    └── adaptadores/
frontend/                 React + Vite
docs/                     modelo ER, diccionario de datos, bitácora, capturas
```

## Instalación desde cero

1. Clonar el repositorio y entrar a `backEnd/`.
2. Crear y activar el entorno virtual:
   - Windows (cmd): `python -m venv entorno` y `entorno\Scripts\activate.bat`
   - Windows (PowerShell): `python -m venv entorno` y `.\entorno\Scripts\Activate.ps1`
   - Linux/Mac: `python -m venv entorno` y `source entorno/bin/activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Copiar `.env.example` a `.env` y completar con los datos de tu esquema de FreeSQL (servicio, usuario y contraseña).
5. En el worksheet de FreeSQL, ejecutar como script `sql/01_crear_tablas.sql` y luego `sql/02_datos_ejemplo.sql`.
6. Probar la conexión: `python manage.py check --database negocio`

La respuesta esperada es `System check identified no issues (0 silenced).`

## Base de datos

- `default` (SQLite): tablas internas de Django (usuarios, tokens, sesiones, migraciones).
- `negocio` (Oracle): solo las cinco tablas del negocio. Un router envía a Oracle los modelos de la aplicación `gimnasio` e impide que las migraciones modifiquen ese esquema.

El modelo entidad-relación y el diccionario de datos están en `docs/`.

## Usuarios de prueba por rol

(Se completa en la Semana 3.)

## Avance semanal

### Semana 1
- Modelo entidad-relación y diccionario de datos (`docs/`).
- Scripts `01_crear_tablas.sql` y `02_datos_ejemplo.sql` ejecutados en FreeSQL, con captura de `user_tables`.
- Proyecto Django `gimnasio_project` con la aplicación `gimnasio` y las carpetas de las cuatro capas.
- Configuración de las dos bases de datos con router y conexión a Oracle probada.
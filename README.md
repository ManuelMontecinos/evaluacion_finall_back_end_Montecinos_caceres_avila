# G05 · Gimnasio «Fuerza Austral»

Proyecto final de Back End (INACAP 2026): API hexagonal con Django, Oracle y React.

## Integrantes

| Integrante | Usuario git | Entidades a cargo |
|---|---|---|
| (nombre) | (usuario) | (por definir) |
| (nombre) | (usuario) | (por definir) |
| (nombre) | (usuario) | (por definir) |

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

## Estructura del repositorio

```
backEnd/   proyecto Django (con sql/ para los scripts de Oracle)
frontend/  React + Vite
docs/      modelo de datos, diccionario, bitácora, colección de Postman
```

## Instalación desde cero

1. Clonar el repositorio y entrar a `backEnd/`.
2. Crear y activar el entorno virtual:
   - Windows: `python -m venv entorno` y `.\entorno\Scripts\Activate.ps1`
   - Linux/Mac: `python -m venv entorno` y `source entorno/bin/activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Copiar `.env.example` a `.env` y completar con los datos de tu esquema de FreeSQL.
5. En el worksheet de FreeSQL, ejecutar como script `sql/01_crear_tablas.sql` y luego `sql/02_datos_ejemplo.sql`.
6. Probar la conexión: `python manage.py check --database negocio`

## Usuarios de prueba por rol

(Se completa en la Semana 3.)

## Avance semanal

- **Semana 1:** (completar)

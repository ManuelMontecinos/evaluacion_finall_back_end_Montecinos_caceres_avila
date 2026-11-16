INSERT INTO planes (nombre, descripcion, precio_mensual, clases_por_semana)
VALUES ('Básico', 'Acceso a clases grupales de lunes a viernes', 24990, 2);
INSERT INTO planes (nombre, descripcion, precio_mensual, clases_por_semana)
VALUES ('Estándar', 'Acceso a todas las clases grupales y sala de máquinas', 34990, 3);
INSERT INTO planes (nombre, descripcion, precio_mensual, clases_por_semana)
VALUES ('Premium', 'Clases grupales ilimitadas en horario completo y evaluación física mensual', 44990, 5);
INSERT INTO planes (nombre, descripcion, precio_mensual, clases_por_semana)
VALUES ('Libre', 'Todas las clases todos los días, incluidos fines de semana', 54990, 7);
INSERT INTO planes (nombre, descripcion, precio_mensual, clases_por_semana)
VALUES ('Estudiante', 'Plan con descuento para estudiantes con credencial vigente', 19990, 2);

INSERT INTO instructores (rut, nombre, especialidad, email, telefono, usuario, activo)
VALUES ('14567890-0', 'Carolina Vargas Soto', 'Yoga', 'carolina.vargas@fuerzaaustral.cl', '+56911223344', 'cvargas', 1);
INSERT INTO instructores (rut, nombre, especialidad, email, telefono, usuario, activo)
VALUES ('16789012-1', 'Matías Fuentes Reyes', 'Spinning', 'matias.fuentes@fuerzaaustral.cl', '+56922334455', 'mfuentes', 1);
INSERT INTO instructores (rut, nombre, especialidad, email, telefono, usuario, activo)
VALUES ('15432109-8', 'Javiera Araya Pino', 'Crossfit', 'javiera.araya@fuerzaaustral.cl', '+56933445566', 'jaraya', 1);
INSERT INTO instructores (rut, nombre, especialidad, email, telefono, usuario, activo)
VALUES ('17890123-0', 'Sebastián Contreras Rojas', 'Funcional', 'sebastian.contreras@fuerzaaustral.cl', '+56944556677', 'scontreras', 1);
INSERT INTO instructores (rut, nombre, especialidad, email, telefono, usuario, activo)
VALUES ('13456789-9', 'Francisca Olivares Mena', 'Pilates', 'francisca.olivares@fuerzaaustral.cl', '+56955667788', 'folivares', 1);

INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('20145873-0', 'Camila Rojas Herrera', 'camila.rojas@correo.cl', '+56981112233',
        (SELECT id_plan FROM planes WHERE nombre = 'Premium'), DATE '2026-12-15', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('19876543-0', 'Benjamín Muñoz Díaz', 'benjamin.munoz@correo.cl', '+56982223344',
        (SELECT id_plan FROM planes WHERE nombre = 'Estándar'), DATE '2026-11-20', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('21034567-1', 'Valentina Pérez Lagos', 'valentina.perez@correo.cl', '+56983334455',
        (SELECT id_plan FROM planes WHERE nombre = 'Básico'), DATE '2026-11-18', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('18765432-7', 'Diego Soto Castillo', 'diego.soto@correo.cl', '+56984445566',
        (SELECT id_plan FROM planes WHERE nombre = 'Libre'), DATE '2027-02-28', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('22345678-2', 'Antonia Navarro Bravo', 'antonia.navarro@correo.cl', NULL,
        (SELECT id_plan FROM planes WHERE nombre = 'Estudiante'), DATE '2026-11-10', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('17654321-3', 'Felipe Gutiérrez Ortiz', 'felipe.gutierrez@correo.cl', '+56985556677',
        (SELECT id_plan FROM planes WHERE nombre = 'Estándar'), DATE '2026-12-31', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('20987654-K', 'Daniela Salazar Ponce', 'daniela.salazar@correo.cl', '+56986667788',
        (SELECT id_plan FROM planes WHERE nombre = 'Premium'), DATE '2026-11-22', 1);
INSERT INTO socios (rut, nombre, email, telefono, id_plan, fecha_vencimiento, activo)
VALUES ('19234567-7', 'Nicolás Espinoza Vera', NULL, '+56987778899',
        (SELECT id_plan FROM planes WHERE nombre = 'Básico'), DATE '2026-10-30', 0);

INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '17890123-0'),
        'Funcional matinal', 'Circuito de fuerza y resistencia', TIMESTAMP '2026-11-09 10:00:00', 12, 'realizada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '14567890-0'),
        'Yoga matutino', 'Hatha yoga para todos los niveles', TIMESTAMP '2026-11-16 10:00:00', 15, 'programada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '16789012-1'),
        'Spinning intensivo', 'Sesión de ciclismo indoor de alta intensidad', TIMESTAMP '2026-11-16 22:00:00', 20, 'programada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '17890123-0'),
        'Funcional vespertino', 'Entrenamiento funcional con peso corporal y mancuernas', TIMESTAMP '2026-11-17 22:00:00', 12, 'programada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '13456789-9'),
        'Pilates mat', 'Pilates en colchoneta para fortalecer el core', TIMESTAMP '2026-11-18 15:00:00', 10, 'programada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '15432109-8'),
        'Crossfit WOD', 'Entrenamiento del día de alta intensidad', TIMESTAMP '2026-11-19 22:00:00', 3, 'programada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '13456789-9'),
        'Pilates avanzado', 'Pilates de nivel avanzado', TIMESTAMP '2026-11-20 15:00:00', 10, 'suspendida');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '14567890-0'),
        'Yoga vespertino', 'Vinyasa yoga para cerrar la semana', TIMESTAMP '2026-11-20 21:00:00', 15, 'programada');
INSERT INTO clases (id_instructor, nombre, descripcion, fecha_hora, cupo_maximo, estado)
VALUES ((SELECT id_instructor FROM instructores WHERE rut = '16789012-1'),
        'Spinning sabatino', 'Ciclismo indoor de fin de semana', TIMESTAMP '2026-11-21 13:00:00', 18, 'programada');

INSERT INTO inscripciones (id_clase, id_socio, fecha_inscripcion, asistio)
SELECT c.id_clase, s.id_socio, TIMESTAMP '2026-11-05 14:30:00', 1
FROM clases c, socios s WHERE c.nombre = 'Funcional matinal' AND s.rut = '20145873-0';
INSERT INTO inscripciones (id_clase, id_socio, fecha_inscripcion, asistio)
SELECT c.id_clase, s.id_socio, TIMESTAMP '2026-11-05 15:10:00', 0
FROM clases c, socios s WHERE c.nombre = 'Funcional matinal' AND s.rut = '19876543-0';
INSERT INTO inscripciones (id_clase, id_socio, fecha_inscripcion, asistio)
SELECT c.id_clase, s.id_socio, TIMESTAMP '2026-11-06 09:45:00', 1
FROM clases c, socios s WHERE c.nombre = 'Funcional matinal' AND s.rut = '18765432-7';
INSERT INTO inscripciones (id_clase, id_socio, fecha_inscripcion, asistio)
SELECT c.id_clase, s.id_socio, TIMESTAMP '2026-11-06 18:20:00', 1
FROM clases c, socios s WHERE c.nombre = 'Funcional matinal' AND s.rut = '17654321-3';
INSERT INTO inscripciones (id_clase, id_socio, fecha_inscripcion, asistio)
SELECT c.id_clase, s.id_socio, TIMESTAMP '2026-11-07 12:00:00', 1
FROM clases c, socios s WHERE c.nombre = 'Funcional matinal' AND s.rut = '22345678-2';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Yoga matutino' AND s.rut = '20145873-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Yoga matutino' AND s.rut = '21034567-1';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Spinning intensivo' AND s.rut = '20145873-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Spinning intensivo' AND s.rut = '19876543-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Spinning intensivo' AND s.rut = '18765432-7';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Funcional vespertino' AND s.rut = '20145873-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Funcional vespertino' AND s.rut = '19876543-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Funcional vespertino' AND s.rut = '17654321-3';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Pilates mat' AND s.rut = '19876543-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Pilates mat' AND s.rut = '21034567-1';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Crossfit WOD' AND s.rut = '18765432-7';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Crossfit WOD' AND s.rut = '17654321-3';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Crossfit WOD' AND s.rut = '20987654-K';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Yoga vespertino' AND s.rut = '20145873-0';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Yoga vespertino' AND s.rut = '17654321-3';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Yoga vespertino' AND s.rut = '20987654-K';

INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Spinning sabatino' AND s.rut = '18765432-7';
INSERT INTO inscripciones (id_clase, id_socio)
SELECT c.id_clase, s.id_socio FROM clases c, socios s WHERE c.nombre = 'Spinning sabatino' AND s.rut = '20987654-K';

COMMIT;

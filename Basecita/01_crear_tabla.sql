CREATE TABLE persona
(
  id SERIAL PRIMARY KEY,
  cedula integer,
  nombre character varying(1000),
  apellido character varying(1000),
  calificacion numeric, 
  comentariocalif character varying(1000),
  materias character varying(1000), 
  fechanacimiento character varying(1000), 
  promedio numeric, 
  historialviajes character varying(1000), 
  infodeviajes character varying(1000), 
  situacioneconomica character varying(1000), 
  anioegreso numeric,
  matriculadocente character varying(1000),
  lugartrabajodocente character varying(1000),
  becar character varying(1000)
);	
	
--select * from persona;
--drop table persona;
INSERT INTO persona (cedula, nombre, apellido, calificacion, comentariocalif, materias, fechanacimiento, promedio, historialviajes, infodeviajes, situacioneconomica, becar,anioegreso, matriculadocente, lugartrabajodocente)
VALUES 
(1234, 'Santiago', 'Rojas', 85, 'Buen estudiante', 'Matemáticas', '1990-05-15', 85, 'Linea 12', 'Linea 12 diferencial', 'Buena', 'NO',NULL, NULL, NULL),
(1111, 'Damian', 'Bobadilla', 77, 'Buen estudiante', 'Fisica', '1999-11-17', 77, 'Linea 96', 'Linea 96 normal', 'Buena', 'NO',NULL, NULL, NULL),
(2222, 'Oscar', 'Romero', 91, 'Excelente estudiante', 'Quimica', '1998-05-10', 91, 'Linea 96', 'Linea 96 nomal', 'Alto', 'NO',NULL, NULL, NULL),
(4321, 'Jessica', 'Martinez', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2009, 'LAB123', 'UNIVESIDAD AAA'),
(9101, 'Marcos', 'Acosta', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2009, 'ABC123', 'UNIVESIDAD AA'),
(5678, 'Jose', 'Leguizamon', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 2010, 'SD2023', 'UNIVESIDAD ABC');

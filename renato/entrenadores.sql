SELECT * FROM public.Entrenadores
ORDER BY id_entrenador ASC 
--Insertar
INSERT INTO public."Entrenadores (Nombre, Edad, Sexo)
VALUES ('Ash Ketchum', 10, 'Masculino');

--Leer 
SELECT * FROM public."Entrenadores";

-- Leer un registro específico
SELECT * FROM public."Entrenadores
WHERE Nombre = 'Ash Ketchum';

--Actualizar 
UPDATE public."Entrenadores"
SET Edad = 11
WHERE Nombre = 'Ash Ketchum';
--Eliminar 
DELETE FROM public."Entrenadores"
WHERE Nombre = 'Ash Ketchum';


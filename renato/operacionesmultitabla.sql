--Insertar Datos en las Tablas Entrenador y Pokemon
-- Insertar datos en la tabla Entrenador
INSERT INTO public.Entrenadores ("Nombre", "Edad", "Sexo")
VALUES ('Ash Ketchum', 10, 'Masculino');

-- Insertar datos en la tabla Pokemon
INSERT INTO "pokemon" ("id_pokemon,"Nombre", "Tipo", "Habilidad", "Estadistica")
VALUES (12,'Charizard', 'Fuego/Volador', 'Mar Llamas', 'v:84 ps:78');
--Relacionar un Entrenador con dos Pokémon
-- Relacionar Ash Ketchum con Pikachu y Charizard
INSERT INTO public."pokemon_entrenador" ("ID_ENTRENADOR", "ID_POKEMON")
VALUES (1, 12);  -- Ash Ketchum (ID 1) y Charizard (ID 2)
SELECT * FROM "pokemon_entrenador"
ORDER BY "id" ASC;

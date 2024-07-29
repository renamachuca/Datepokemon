INSERT INTO public."pokemon_entrenador"(
	"ID_ENTRENADOR", "ID_POKEMON")
	VALUES (8,8);
SELECT * FROM "Entrenador_pokemon"
ORDER BY "id" ASC
--REALIZAR MULTITABLE (CONSULTA DE POKEMON Y JUGADOR)
SELECT e."Nombre" AS Entrenadores, p."Nombre" AS pokemon
FROM "Entrenador" e
JOIN "Entrenador_pokemon" ep ON e."Id" = ep."ID_ENTRENADOR"
JOIN "pokemon" p ON ep."ID_POKEMON" = p."Id"
WHERE e."Nombre" = 'Teniente Surge';

SELECT * FROM "Entrenadores"
ORDER BY "id_entrenador" ASC	
INSERT INTO Entrenadores VALUES (15,' Israel',13, 'Masculino');
INSERT INTO Entrenadores VALUES (16,'Bruno',13, 'Masculino');
DELETE FROM Entrenadores
WHERE id_entrenador = 15
UPDATE Entrenadores
SET "Nombre" = 'blaine'
WHERE id_pokemon = 4;



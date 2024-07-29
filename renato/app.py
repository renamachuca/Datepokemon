from flask import Flask, request, jsonify, render_template, url_for, redirect
from conexion import get_conexion

app = Flask(__name__)


# Ruta para mostrar la lista de Pokémon
@app.route('/', methods=['GET'])
def index():
    conn = None
    try:
        conn = get_conexion()  # Usa la función importada
        if conn is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'})
        
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM pokemon
            ORDER BY id_pokemon ASC;  -- Ordena por id_pokemon en orden ascendente
        ''')
        
        pokemones = cursor.fetchall()
        pokemon_list = [
            {
                'id_pokemon': p[0],
                'nombre': p[1],
                'tipo': p[2],
                'habilidad': p[3],
                'estadisticas': p[4]
            }
            for p in pokemones
        ]
        
        return render_template('index.html', pokemones=pokemon_list)
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    finally:
        if conn is not None and not conn.closed:
            conn.close()



# Ruta para mostrar el formulario de inserción y manejar la inserción de datos
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id_pokemon = request.form['id_pokemon']
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        habilidad = request.form['habilidad']
        estadisticas = request.form['estadisticas']
        
        conn = None
        try:
            conn = get_conexion()
            if conn is None:
                return jsonify({'error': 'no se pudo conectar a la base de datos'})
            
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pokemon (id_pokemon, nombre, tipo, habilidad, estadisticas)
                VALUES (%s, %s, %s, %s, %s)
            ''', (id_pokemon, nombre, tipo, habilidad, estadisticas))
            conn.commit()
            return redirect(url_for('index'))

        except Exception as e:
            return jsonify({'error': str(e)})

        finally:
            if conn is not None and not conn.closed:
                conn.close()
    else:
        return render_template('add.html')

## Ruta para mostrar el formulario de edición y manejar la edición de datos
@app.route('/edit/<int:id_pokemon>', methods=['GET', 'POST'])
def edit(id_pokemon):
    conn = None
    try:
        conn = get_conexion()
        if conn is None:
            return jsonify({'error': 'no se pudo conectar a la base de datos'})

        if request.method == 'POST':
            nombre = request.form.get('nombre')
            tipo = request.form.get('tipo')
            habilidad = request.form.get('habilidad')
            estadisticas = request.form.get('estadisticas')

            cursor = conn.cursor()
            cursor.execute('''
                UPDATE pokemon
                SET nombre = %s, tipo = %s, habilidad = %s, estadisticas = %s
                WHERE id_pokemon = %s
            ''', (nombre, tipo, habilidad, estadisticas, id_pokemon))
            conn.commit()
            return redirect(url_for('index'))
        
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pokemon WHERE id_pokemon = %s', (id_pokemon,))
        pokemon = cursor.fetchone()
        if pokemon is None:
            return jsonify({'error': 'Pokemon no encontrado'})

        return render_template('edit.html', pokemon=pokemon)
    
    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        if conn is not None and not conn.closed:
            conn.close()



@app.route('/delete/<int:id_pokemon>', methods=['POST'])
def delete(id_pokemon):
    conn = None
    try:
        conn = get_conexion()
        if conn is None:
            return jsonify({'error': 'no se pudo conectar a la base de datos'})

        cursor = conn.cursor()
        cursor.execute('DELETE FROM pokemon WHERE id_pokemon = %s', (id_pokemon,))
        conn.commit()
        return redirect(url_for('index'))
    
    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        if conn is not None and not conn.closed:
            conn.close()




@app.route('/entrenadores', methods=['GET'])
def mostrar_entrenadores():
    conn = None
    try:
        conn = get_conexion()  # Usa la función importada
        if conn is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'})
        
        cursor = conn.cursor()
        
        # Consulta para obtener entrenadores y sus Pokémon, ordenados por la cantidad de Pokémon
        cursor.execute('''
            SELECT e.id_entrenador, e.nombre, COUNT(pe.id_pokemon) as cantidad_pokemones
            FROM public.entrenadores e
            LEFT JOIN public.pokemon_entrenador pe ON e.id_entrenador = pe.id_entrenador
            GROUP BY e.id_entrenador, e.nombre
            ORDER BY cantidad_pokemones DESC;
        ''')
        
        entrenadores = cursor.fetchall()
        
        # Imprimir entrenadores para depuración
        print("Entrenadores obtenidos:", entrenadores)
        
        # Crear una lista de entrenadores con sus respectivos Pokémon
        entrenadores_list = []
        for entrenador in entrenadores:
            cursor.execute('''
                SELECT p.id_pokemon, p.nombre, p.tipo, p.habilidad, p.estadisticas
                FROM public.pokemon p
                INNER JOIN public.pokemon_entrenador pe ON p.id_pokemon = pe.id_pokemon
                WHERE pe.id_entrenador = %s
                ORDER BY p.nombre;
            ''', (entrenador[0],))
            pokemones = cursor.fetchall()
            entrenadores_list.append({
                'id_entrenador': entrenador[0],
                'nombre': entrenador[1],
                'cantidad_pokemones': entrenador[2],
                'pokemones': [{
                    'id_pokemon': p[0],
                    'nombre': p[1],
                    'tipo': p[2],
                    'habilidad': p[3],
                    'estadisticas': p[4]
                } for p in pokemones]
            })
        
        # Imprimir lista de entrenadores para depuración
        print("Lista de entrenadores:", entrenadores_list)
        
        return render_template('entrenadores.html', entrenadores=entrenadores_list)
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    finally:
        if conn is not None and not conn.closed:
            conn.close()


@app.route('/batalla', methods=['GET'])
def mostrar_batalla():
    conn = None
    try:
        conn = get_conexion()  # Usa la función importada
        if conn is None:
            return jsonify({'error': 'No se pudo conectar a la base de datos'})
        
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM batalla ORDER BY id_batalla ASC;')
        batallas = cursor.fetchall()
        
        batalla_list = [
            {
                'id_batalla': b[0],
                'entrenador_1': b[1],
                'entrenador_2': b[2],
                'entrenador_ganador_id': b[3],
                'entrenador_perdedor_id': b[4],
                'id_pokemon1': b[5],
                'id_pokemon2': b[6]
            }
            for b in batallas
        ]
        
        return render_template('batalla.html', batallas=batalla_list)
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
    finally:
        if conn is not None and not conn.closed:
            conn.close()




if __name__ == '__main__':
    app.run(debug=True)
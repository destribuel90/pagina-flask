from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'ini98Yul'
DB_NAME = 'prueba_apirest'

@app.route('/')
def routin():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    cursor = None
    try:
        data = request.get_json()
        if 'Nombre' not in data or 'Edad' not in data or 'Especie' not in data:
            return jsonify({'message': 'Faltan datos'})
        
        nombre = data['Nombre']
        edad = data['Edad']
        especie = data['Especie']

        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        cursor = conn.cursor()
        sql = "INSERT INTO user (Nombre, Edad, Especie) VALUES (%s,%s,%s)"
        cursor.execute(sql, (nombre, int(edad), especie))
        conn.commit()
        return jsonify({'message': 'Correcto'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
@app.route('/obtener')
def obtener():
    cursor = None
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        cursor = conn.cursor()
        sql = "SELECT * FROM user"
        cursor.execute(sql) 
        datos = cursor.fetchall()
        personas = []
        for fila in datos:
            persona={'id': fila[0],'Nombre': fila[1],'Edad': fila[2],'Especie': fila[3],'Fecha':fila[4]}
            personas.append(persona)
        
        return jsonify({'Personas':personas,'message':"personas listadas"})
             
    except Exception as e:
        return jsonify({'error': "100"})
    finally:
        if conn:
            conn.close
        if cursor:
            cursor.close    

@app.route('/obtener/<nombre>')
def obtener_persona(nombre):
    conn = None
    cursor = None
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        cursor = conn.cursor()
        sql = "SELECT * FROM user WHERE Nombre = %s"
        cursor.execute(sql, (nombre,))
        datos = cursor.fetchone()
        if datos is not None:
            persona = {
                'id': datos[0],
                'Nombre': datos[1],
                'Edad': datos[2],
                'Especie': datos[3],
                'Fecha': datos[4]
            }
            return jsonify({'Persona': persona, 'message': "correcto"})
        else:
            return jsonify({'message': "Persona no encontrada"})
    except Exception as e:
        return jsonify({'Error': str(e)})
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    conn = None
    cursor = None
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        cursor = conn.cursor()
        data = request.get_json()
        if 'Nombre' not in data or 'Edad' not in data:
           return jsonify({'message': "Error"})
        new_nombre = data['Nombre']
        new_edad= data['Edad']
        sql = "UPDATE user SET Nombre = %s, Edad = %s WHERE id = %s"
        cursor.execute(sql, (new_nombre, new_edad, id))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': "Error: ID no encontrado"}), 404
        return jsonify({'message': "Correcto"})
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"})
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    conn = None
    cursor = None
    try:
        conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)
        cursor = conn.cursor()
        sql = "DELETE FROM user WHERE id = %s"
        cursor.execute(sql, (id,))
        conn.commit()
        if cursor.rowcount > 0:
            return jsonify({'message': "Eliminado correctamente"})
        else:
            return jsonify({'message': "No se encontró el registro para eliminar"})
    except Exception as e:
        return jsonify({'message': f"Error: {str(e)}"})
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug= True)




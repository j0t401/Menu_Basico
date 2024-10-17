from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="psw@Sena2024",
    database="muen_prueba"
)

# Ruta para mostrar la página web y cargar datos de la base de datos
@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    if request.is_json:
        return jsonify(data)
    return render_template('index.html', usuarios=data)

# Ruta para insertar un usuario
@app.route('/insertar_usuario', methods=['POST'])
def insertar_usuario():
    data = request.json
    usuario = data['Usuario']
    email = data['Email']

    cursor = db.cursor()
    query = "INSERT INTO data (Usuario, Email) VALUES (%s, %s)"
    cursor.execute(query, (usuario, email))
    db.commit()

    return jsonify({'status': 'Usuario insertado con éxito'})

# Ruta para eliminar un usuario
@app.route('/eliminar_usuario', methods=['POST'])
def eliminar_usuario():
    id_data = request.json['iddata']
    
    cursor = db.cursor()
    query = "DELETE FROM data WHERE id = %s"
    cursor.execute(query, (id_data,))
    db.commit()
    
    return jsonify({'status': 'Usuario eliminado'})

# Ruta para actualizar un usuario
@app.route('/actualizar_usuario', methods=['POST'])
def actualizar_usuario():
    data = request.json
    id_data = data['iddata']
    usuario = data['Usuario']
    email = data['Email']

    cursor = db.cursor()
    query = "UPDATE data SET Usuario = %s, Email = %s WHERE id = %s"
    cursor.execute(query, (usuario, email, id_data))
    db.commit()

    return jsonify({'status': 'Usuario actualizado'})

if __name__ == '__main__':
    app.run(debug=True)

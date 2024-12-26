from flask import Flask, request, jsonify, render_template, send_file
import sqlite3
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)

# Database setup
DATABASE = 'cars.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Drop the table if it exists to ensure schema consistency
        cursor.execute("DROP TABLE IF EXISTS cars")
        
        # Create the cars table
        cursor.execute('''
        CREATE TABLE cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            length REAL,
            weight REAL,
            velocity REAL,
            color TEXT
        )
        ''')
        
        # Insert sample data
        cursor.execute("INSERT INTO cars (length, weight, velocity, color) VALUES (4.5, 1200, 200, 'red')")
        cursor.execute("INSERT INTO cars (length, weight, velocity, color) VALUES (4.2, 1100, 180, 'blue')")
        cursor.execute("INSERT INTO cars (length, weight, velocity, color) VALUES (4.8, 1500, 220, 'black')")
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    length = request.args.get('length')
    weight = request.args.get('weight')
    velocity = request.args.get('velocity')
    color = request.args.get('color')
    
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    if length:
        query += " AND length = ?"
        params.append(length)
    if weight:
        query += " AND weight = ?"
        params.append(weight)
    if velocity:
        query += " AND velocity = ?"
        params.append(velocity)
    if color:
        query += " AND color = ?"
        params.append(color)

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

    cars = [
        {'id': row[0], 'length': row[1], 'weight': row[2], 'velocity': row[3], 'color': row[4]}
        for row in results
    ]
    return jsonify(cars)

@app.route('/download', methods=['GET'])
def download():
    length = request.args.get('length')
    weight = request.args.get('weight')
    velocity = request.args.get('velocity')
    color = request.args.get('color')
    
    query = "SELECT * FROM cars WHERE 1=1"
    params = []

    if length:
        query += " AND length = ?"
        params.append(length)
    if weight:
        query += " AND weight = ?"
        params.append(weight)
    if velocity:
        query += " AND velocity = ?"
        params.append(velocity)
    if color:
        query += " AND color = ?"
        params.append(color)

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

    root = ET.Element("cars")
    for row in results:
        car = ET.SubElement(root, "car")
        ET.SubElement(car, "id").text = str(row[0])
        ET.SubElement(car, "length").text = str(row[1])
        ET.SubElement(car, "weight").text = str(row[2])
        ET.SubElement(car, "velocity").text = str(row[3])
        ET.SubElement(car, "color").text = row[4]

    file_name = 'cars.xml'
    with open(file_name, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f)

    try:
        # Send file to client and delete afterward
        response = send_file(file_name, as_attachment=True)
        response.call_on_close(lambda: os.remove(file_name))  # Deletes the file after sending
        return response
    except Exception:
        if os.path.exists(file_name):
            os.remove(file_name)  # Cleanup on exception
        raise


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

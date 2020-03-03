from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/temp', methods=["POST"])
def temp():
    payload = request.get_json(force=True)
    temp = payload['temp']
    conn = sqlite3.connect('read_temp_hum.db')
    c = conn.cursor()
    c.execute('INSERT INTO records(temp) VALUES(?)', (temp,))
    conn.commit()
    conn.close()
    resp = {'status':'OK'}
    return jsonify(resp)

@app.route('/hum', methods=["POST"])
def hum():
    payload = request.get_json(force=True)
    hum = payload['hum']
    conn = sqlite3.connect('read_temp_hum.db')
    c = conn.cursor()
    c.execute('INSERT INTO records(hum) VALUES(?)', (hum,))
    conn.commit()
    conn.close()
    resp = {'status':'OK'}
    return jsonify(resp)

@app.route('/summary', methods=["GET"])
def summary():
    conn = sqlite3.connect('read_temp_hum.db')
    c = conn.cursor()
    c.execute('SELECT * FROM records')
    records = c.fetchall()
    results = []
    for r in records:
        if len(r) == 2:
            results.append({'timestamp':r[1], 'temp':r[2], 'hum':r[3]})
        elif (r[2]):
            results.append({'timestamp':r[1], 'temp':r[2]})
        elif (r[3]):
            results.append({'timestamp':r[1], 'hum':r[3]})
    conn.commit()
    conn.close()
    resp = {'status':'OK', 'results':results}
    return jsonify(resp)

if __name__ == '__main__':
    conn = sqlite3.connect('read_temp_hum.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS records
             (_id INTEGER PRIMARY KEY AUTOINCREMENT,
             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
             temp TEXT , 
             hum TEXT )''')
    conn.commit()
    conn.close()
    app.run(debug=True)

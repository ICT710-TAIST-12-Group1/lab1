from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/update', methods=["POST"])
def update():
    payload = request.get_json(force=True)
    temp = payload['temp']
    humid = payload['humid']
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    c.execute('INSERT INTO label(temp,humid) VALUES(%s,%s);', (temp,humid))
    conn.commit()
    conn.close()
    resp = {'status':'OK'}
    return jsonify(resp)

@app.route('/query', methods=["GET"])
def query():
    temp = request.args.get('temp')
    humid = request.args.get('humid')
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()
    c.execute('SELECT * FROM label;')
    records = c.fetchall()
    results = []
    for r in records:
        results.append({'timestamp':r[1], 'temp':r[2] , 'humid':r[3]})
    conn.commit()
    conn.close()
    resp = {'status':'OK', 'results':results}
    return jsonify(resp)

if __name__ == '__main__':

    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    c = conn.cursor()   
    c.execute('''CREATE TABLE IF NOT EXISTS label
             (_id SERIAL PRIMARY KEY,
             DATATIMESTAMP timestamp without time zone DEFAULT now(),
             temp INTEGER NOT NULL,
             humid INTEGER NOT NULL);''')
    conn.commit()
    conn.close() 
    app.run(debug=True)

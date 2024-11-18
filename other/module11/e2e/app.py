from flask import Flask, render_template, request
from data import MERGED_DATA

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').strip().lower()
    results = [
        item for item in MERGED_DATA 
        if query in item['code'].lower() or query in item['description'].lower()
    ]
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5005')

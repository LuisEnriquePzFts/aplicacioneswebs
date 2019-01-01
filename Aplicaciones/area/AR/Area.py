# IMPORTA FLASK
from flask import Flask, render_template, request
from modulo import area
app = Flask(__name__)

@app.route('/area', methods=['POST'])
def index():
    
    title = 'Estos son los resultados:'
    radio=float(request.form['radio'])
    

    results = area(radio)
    
    return render_template('results.html',
                           the_title=title,
                           the_radio=radio,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido al Calculador de Área de la Esfera web!')

if __name__ == '__main__':
    app.run(debug=True)

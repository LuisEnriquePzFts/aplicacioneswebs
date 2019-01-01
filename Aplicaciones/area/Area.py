# IMPORTA FLASK
from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('entry.html')

@app.route('/area', methods=['POST'])




def area():
    title = 'Estos son los resultados:'
    radio =request.form['radio']
    a=4
    b=3.1416
    c=2
    results =(float(a)*float(b)*float(radio)**float(c))


    print(results)
    
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

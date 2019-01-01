# IMPORTA FLASK
from flask import Flask, render_template, request
import math
app = Flask(__name__)


@app.route('/')
def index():
    title = 'Estos son los resultados'
    masa=float(request.form['masa'])
    velocidad=float(request.form['velocidad'])

    results = area(masa,velocidad)

    return render_template('results.html',
                           the_title=title,
                           the_radio=radio,
                           the_results=results,)


    
    return render_template('results.html',
                           the_title=title,
                           the_masa=masa,
                           the_velocidad=velocidad,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Bienvenido al Calculador !')

if __name__ == '__main__':
    app.run(debug=True)

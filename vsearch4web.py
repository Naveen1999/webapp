import flask
from vsearch import search4letters
app=flask.Flask(__name__)
@app.route('/')
def hello():
    return flask.redirect('/entry')
@app.route('/search4',methods=['POST'])
def dosearch():
    phrase=flask.request.form['phrase2']
    letters=flask.request.form['letters2']
    title='Here are your results'
    results=str(search4letters(phrase,letters))
    return flask.render_template('results.html',title=title,phrase=phrase,letters=letters,results=results)
@app.route('/entry')
def entry():
    return flask.render_template('entry.html',title='searching for web')
app.run(debug=True)

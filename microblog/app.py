from flask import flask

app = flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo!'

if __name__ == '__main__':
    app.run()
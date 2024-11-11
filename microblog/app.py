from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/contato')
def contato():
  return render_template("contato.html", tel="(87) 9999888888")

@app.route('/sobre')
def sobre():
  return render_template("sobre.html")

if __name__ == '__main__':
    app.run()
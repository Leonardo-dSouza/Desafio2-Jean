from flask import Flask, render_template
app = Flask("__name__")



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")







if __name__ == '__main__':
    app.run(debug=True)
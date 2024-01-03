from flask import Flask

app = Flask(__name__)


@app.route("/")

def greet():
    return "<h1 style='color:blue'>This is flask</h1>"

@app.route("/help")
def help():
    return "<h1>Any Help ?</h1>"

if __name__ == '__main__':
    app.run(debug=True)

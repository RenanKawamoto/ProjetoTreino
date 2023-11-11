# Importando o flask
from flask import Flask
from controllers.home_controller import home_controller

# criou uma variavel da intancia Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return home_controller()

if __name__  == '__main__':
    app.run()
from flask import Flask
from pyfladesk import init_gui


app = Flask(__name__, static_folder='static/')


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    # app.run()
    init_gui(app)

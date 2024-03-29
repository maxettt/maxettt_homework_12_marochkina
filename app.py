from flask import Flask, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/uploads/images/<path:path>')
def static_dir(path):
    return send_from_directory('uploads/images/', path)

app.run(debug=False)


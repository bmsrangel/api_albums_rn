from flask import Flask
from flask import render_template
import os


def create_app(config_filename):
    app = Flask(__name__, static_folder="./templates")
    app.config.from_object(config_filename)

    @app.route('/')
    def index():
        return render_template('index.html')

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        app.run(host='localhost', port=5000, debug=True)

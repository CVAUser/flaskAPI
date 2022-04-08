import os
from flask import Flask

#instance_relative_config=True tells the app that configuration files 
# are relative to the instance folder. 
# The instance folder is located outside the flaskr package
app = Flask(__name__, instance_relative_config=True)

def create_app(test_config=None):
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

from app import routes
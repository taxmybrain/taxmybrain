import os
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        ) # These settings are overridden by the pyfile config settings
    
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
        # app.config.from_envvar('CONFIG_SETTINGS')
    else:
        # Load the test config if passed in
        app.config.from_pyfile('test_config.py')
    
     # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    bootstrap = Bootstrap(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .main.templatefilters import blueprint
    app.register_blueprint(blueprint)
    
    return app


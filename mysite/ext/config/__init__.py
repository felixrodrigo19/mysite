def init_app(app):
    app.config["SECRET_KEY"] = "ite123"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mysite.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
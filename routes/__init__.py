from controllers.hello import hello_bp
from controllers.user import user_bp
from controllers.auth import auth_bp
from controllers.notification import notification_bp
class Router:
    def __init__(self,app):
        self.app=app
        self.routes()
    def routes(self):
        self.app.register_blueprint(
            hello_bp,
            url_prefix="/api/v1/hello")
        self.app.register_blueprint(
            user_bp,
            url_prefix='/api/v1/user'
        )
        self.app.register_blueprint(
            auth_bp,
            url_prefix='/api/v1/auth'
        )
        self.app.register_blueprint(
            notification_bp,
            url_prefix='/api/v1/notification'
        )
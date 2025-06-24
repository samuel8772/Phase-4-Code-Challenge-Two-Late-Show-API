from flask import Flask, jsonify, make_response
from server.config import Config
from server.extensions import db, migrate, jwt, bcrypt
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Define basic routes before blueprint registration
    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Late Show API"})

    @app.route('/api/test', methods=['POST'])
    def test():
        print("🔥 Test route hit!")  # Check terminal for this
        return {"message": "Test successful"}, 200

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    # Register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.appearance_controller import appearance_bp

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(episode_bp, url_prefix='/api')
    app.register_blueprint(guest_bp, url_prefix='/api')
    app.register_blueprint(appearance_bp, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

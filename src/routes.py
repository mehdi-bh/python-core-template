from flask import jsonify

def init_routes(app):
    @app.route('/')
    def home():
        return jsonify({"message": "Hello, World!"})

    @app.route('/api/data')
    def get_data():
        return jsonify({"data": "Some data here"})

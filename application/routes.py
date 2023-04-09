from flask import jsonify
from flask import Flask, render_template
from redis import Redis

redis = Redis(host='redis', port=6379)

def init_routes(app):
    @app.route("/api", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "todos api is up",
            "success": True,
            "data": None
        }), 200

    @app.route('/')
    def home():
        return render_template("index.html")
    @app.route('/redis')
    def hello():
        redis.incr('hits')
        counter = str(redis.get('hits'),'utf-8')
        return "This webpage has been viewed "+counter+" time(s)"
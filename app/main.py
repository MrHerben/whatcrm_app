from aiohttp import web
from routes import setup_routes
from utils import setup_logging
from config import Config

def create_app():
    setup_logging()
    app = web.Application()
    setup_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host=Config.HOST, port=Config.PORT)

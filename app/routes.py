from handlers import get_tariffs

def setup_routes(app):
    app.router.add_get("/", get_tariffs)

from .restaurant_controller import restaurants_bp
from .pizza_controller import pizzas_bp
from .restaurant_pizza_controller import restaurant_pizzas_bp

def register_blueprints(app):
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(restaurant_pizzas_bp)
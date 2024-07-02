# #!/usr/bin/env python3
# from models import db, Restaurant, RestaurantPizza, Pizza
# from flask_migrate import Migrate
# from flask import Flask, request, jsonify
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.json.compact = False

# migrate = Migrate(app, db)
# db.init_app(app)

# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"

# @app.route('/restaurants', methods=['GET'])
# def get_restaurants():
#     restaurants = Restaurant.query.all()
#     return jsonify([{
#         "id": restaurant.id,
#         "name": restaurant.name,
#         "address": restaurant.address
#     } for restaurant in restaurants])

# @app.route('/restaurants/<int:id>', methods=['GET'])
# def get_restaurant(id):
#     restaurant = Restaurant.query.get(id)
#     if not restaurant:
#         return jsonify({'error': 'Restaurant not found'}), 404
    
#     restaurant_data = {
#         'id': restaurant.id,
#         'name': restaurant.name,
#         'address': restaurant.address,
#         'restaurant_pizzas': [
#             {
#                 'id': rp.id,
#                 'price': rp.price,
#                 'pizza': {
#                     'id': rp.pizza.id,
#                     'name': rp.pizza.name,
#                     'ingredients': rp.pizza.ingredients
#                 }
#             } for rp in restaurant.restaurant_pizza
#         ]
#     }
    
#     return jsonify(restaurant_data)

# @app.route('/restaurants/<int:id>', methods=['DELETE'])
# def delete_restaurant(id):
#     restaurant = Restaurant.query.get(id)
#     if not restaurant:
#         return jsonify({"error": "Restaurant not found"}), 404
    
#     db.session.delete(restaurant)
#     db.session.commit()
#     return jsonify({}), 204

# @app.route('/pizzas', methods=['GET'])
# def get_pizzas():
#     pizzas = Pizza.query.all()
#     return jsonify([{
#         "id": pizza.id,
#         "ingredients": pizza.ingredients,
#         "name": pizza.name
#     } for pizza in pizzas])

# @app.route('/restaurant_pizzas', methods=['POST'])
# def assign_restaurant_pizzas():
#     data = request.get_json()
    
#     # Check if all required fields are present in the request
#     if not data or "pizza_id" not in data or "restaurant_id" not in data or "price" not in data:
#         return jsonify({"error": "Validation failed. Missing pizza_id, restaurant_id, or price in request."}), 400
    
#     # Convert relevant data to integers and validate price range
#     try:
#         pizza_id = int(data["pizza_id"])
#         restaurant_id = int(data["restaurant_id"])
#         price = int(data["price"])
#     except ValueError:
#         return jsonify({"error": "Validation failed. Invalid data types for pizza_id, restaurant_id, or price."}), 400
    
#     # Validate price range
#     if not (1 <= price <= 30):
#         return jsonify({"error": "Validation failed. Price must be between 1 and 30."}), 400
    
#     # Check if Pizza and Restaurant exist
#     pizza = Pizza.query.get(pizza_id)
#     restaurant = Restaurant.query.get(restaurant_id)
    
#     if not pizza or not restaurant:
#         return jsonify({"error": "Validation failed. Pizza or Restaurant not found."}), 400
    
#     # Create and save new RestaurantPizza entry
#     new_rp = RestaurantPizza(
#         price=price,
#         restaurant_id=restaurant_id,
#         pizza_id=pizza_id
#     )
    
#     db.session.add(new_rp)
#     db.session.commit()
    
#     # Return the newly created entry in JSON format
#     return jsonify({
#         "id": new_rp.id,
#         "pizza": {
#             "id": pizza.id,
#             "name": pizza.name,
#             "ingredients": pizza.ingredients
#         },
#         "pizza_id": new_rp.pizza_id,
#         "price": new_rp.price,
#         "restaurant": {
#             "id": restaurant.id,
#             "name": restaurant.name,
#             "address": restaurant.address
#         },
#         "restaurant_id": new_rp.restaurant_id
#     }), 201


# if __name__ == "__main__":
#     app.run(port=5555, debug=True)
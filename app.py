from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

# Data contoh produk smartphone
smartphone_products = [
    {"id": "1", "name": "Smartphone A", "description": "High-performance smartphone with a great camera.", "price": 2500000},
    {"id": "2", "name": "Smartphone B", "description": "Affordable smartphone with essential features.", "price": 1500000},
    {"id": "3", "name": "Smartphone C", "description": "Flagship smartphone with cutting-edge technology.", "price": 5000000},
    {"id": "4", "name": "Smartphone D", "description": "Compact design with a long-lasting battery.", "price": 2000000},
    {"id": "5", "name": "Smartphone E", "description": "Gaming smartphone with high refresh rate display.", "price": 3000000},
    {"id": "6", "name": "Smartphone F", "description": "Stylish smartphone with a unique design.", "price": 2800000},
    {"id": "7", "name": "Smartphone G", "description": "Smartphone with excellent audio quality.", "price": 2200000},
    {"id": "8", "name": "Smartphone H", "description": "Large screen smartphone perfect for multimedia.", "price": 3500000},
    {"id": "9", "name": "Smartphone I", "description": "Smartphone with advanced security features.", "price": 3300000},
    {"id": "10", "name": "Smartphone J", "description": "Lightweight smartphone for everyday use.", "price": 1200000}
]

# Detail produk smartphone
product_details = {product['id']: product for product in smartphone_products}

app = Flask(__name__)
api = Api(app)

class ProductList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(smartphone_products),
            "products": smartphone_products
        }

class ProductDetail(Resource):
    def get(self, product_id):
        if product_id in product_details:
            return {
                "error": False,
                "message": "success",
                "product": product_details[product_id]
            }
        return {"error": True, "message": "Product not found"}, 404

class AddProduct(Resource):
    def post(self):
        data = request.get_json()
        new_product = {
            "id": str(len(smartphone_products) + 1),  # Generate a new ID
            "name": data.get('name'),
            "description": data.get('description'),
            "price": data.get('price')
        }
        smartphone_products.append(new_product)
        product_details[new_product['id']] = new_product
        return {
            "error": False,
            "message": "Product added successfully",
            "product": new_product
        }, 201

class UpdateProduct(Resource):
    def put(self, product_id):
        data = request.get_json()
        if product_id in product_details:
            product_to_update = product_details[product_id]
            product_to_update['name'] = data.get('name', product_to_update['name'])
            product_to_update['description'] = data.get('description', product_to_update['description'])
            product_to_update['price'] = data.get('price', product_to_update['price'])
            return {
                "error": False,
                "message": "Product updated successfully",
                "product": product_to_update
            }
        return {"error": True, "message": "Product not found"}, 404

class DeleteProduct(Resource):
    def delete(self, product_id):
        if product_id in product_details:
            smartphone_products.remove(product_details[product_id])
            del product_details[product_id]
            return {
                "error": False,
                "message": "Product deleted successfully"
            }
        return {"error": True, "message": "Product not found"}, 404

# Menambahkan resource ke API
api.add_resource(ProductList, '/products')
api.add_resource(ProductDetail, '/products/<string:product_id>')
api.add_resource(AddProduct, '/products/add')
api.add_resource(UpdateProduct, '/products/update/<string:product_id>')
api.add_resource(DeleteProduct, '/products/delete/<string:product_id>')

if __name__ == '__main__':
    app.run(debug=True)

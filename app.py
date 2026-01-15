from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Product data structure
products = {
    "tv": [
        {
            "id": 1,
            "name": "Samsung 55-inch QLED TV",
            "price": 1299.99,
            "brand": "Samsung",
            "specs": {
                "screen_size": "55 inches",
                "resolution": "4K UHD",
                "display_type": "QLED",
                "smart_tv": True,
                "hdr": True
            }
        },
        {
            "id": 2,
            "name": "LG 65-inch OLED TV",
            "price": 1999.99,
            "brand": "LG",
            "specs": {
                "screen_size": "65 inches",
                "resolution": "4K UHD",
                "display_type": "OLED",
                "smart_tv": True,
                "hdr": True
            }
        },
        {
            "id": 3,
            "name": "Sony 43-inch LED TV",
            "price": 599.99,
            "brand": "Sony",
            "specs": {
                "screen_size": "43 inches",
                "resolution": "Full HD",
                "display_type": "LED",
                "smart_tv": True,
                "hdr": False
            }
        }
    ],
    "mobile": [
        {
            "id": 1,
            "name": "iPhone 15 Pro",
            "price": 999.99,
            "brand": "Apple",
            "specs": {
                "storage": "128GB",
                "ram": "8GB",
                "screen_size": "6.1 inches",
                "camera": "48MP",
                "battery": "3274 mAh"
            }
        },
        {
            "id": 2,
            "name": "Samsung Galaxy S24",
            "price": 899.99,
            "brand": "Samsung",
            "specs": {
                "storage": "256GB",
                "ram": "8GB",
                "screen_size": "6.2 inches",
                "camera": "50MP",
                "battery": "4000 mAh"
            }
        },
        {
            "id": 3,
            "name": "Google Pixel 8",
            "price": 699.99,
            "brand": "Google",
            "specs": {
                "storage": "128GB",
                "ram": "8GB",
                "screen_size": "6.2 inches",
                "camera": "50MP",
                "battery": "4575 mAh"
            }
        }
    ],
    "laptop": [
        {
            "id": 1,
            "name": "MacBook Pro 14-inch",
            "price": 1999.99,
            "brand": "Apple",
            "specs": {
                "processor": "Apple M3",
                "ram": "16GB",
                "storage": "512GB SSD",
                "screen_size": "14.2 inches",
                "graphics": "Integrated"
            }
        },
        {
            "id": 2,
            "name": "Dell XPS 15",
            "price": 1799.99,
            "brand": "Dell",
            "specs": {
                "processor": "Intel Core i7",
                "ram": "16GB",
                "storage": "512GB SSD",
                "screen_size": "15.6 inches",
                "graphics": "NVIDIA RTX 4050"
            }
        }
    ]
}

@app.route('/', methods=['GET'])
def home():
    """Home route with API information and available endpoints"""
    return jsonify({
        "message": "Product API",
        "version": "1.0.0",
        "endpoints": {
            "home": "/",
            "all_products": "/products",
            "products_by_category": "/products/<category>",
            "specific_product": "/product/<category>/<id>",
            "categories": "/categories",
            "health": "/health"
        },
        "available_categories": ["tv", "mobile", "laptop"]
    })

@app.route('/products', methods=['GET'])
def get_all_products():
    """Returns all products from all categories"""
    all_products = []
    for category, category_products in products.items():
        for product in category_products:
            product_with_category = product.copy()
            product_with_category["category"] = category
            all_products.append(product_with_category)
    return jsonify(all_products)

@app.route('/products/<category>', methods=['GET'])
def get_products_by_category(category):
    """Returns products filtered by category"""
    category = category.lower()
    if category not in products:
        return jsonify({"error": "Category not found", "available_categories": list(products.keys())}), 404
    
    category_products = []
    for product in products[category]:
        product_with_category = product.copy()
        product_with_category["category"] = category
        category_products.append(product_with_category)
    
    return jsonify(category_products)

@app.route('/product/<category>/<int:product_id>', methods=['GET'])
def get_product_by_id(category, product_id):
    """Returns a single product by category and ID"""
    category = category.lower()
    if category not in products:
        return jsonify({"error": "Category not found", "available_categories": list(products.keys())}), 404
    
    product = next((p for p in products[category] if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    product_with_category = product.copy()
    product_with_category["category"] = category
    return jsonify(product_with_category)

@app.route('/categories', methods=['GET'])
def get_categories():
    """Returns all available categories"""
    return jsonify({
        "categories": list(products.keys()),
        "count": len(products)
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

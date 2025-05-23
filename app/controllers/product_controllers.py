from flask import Flask
from app.models.product_model import Product
from flask import blueprints, request, jsonify #the blueprints are for verifying the product and jsonify for giving access to create a new product
from app.extensions import db
from app.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR

product = blueprints("/product", __name__,url_prefix_ = 'api/v1/product') #this is the endpoint

# GET a product
@product.route('/Products', methods=['GET'])
def get_product():
    product = Product.query.all()  # Fetch a product from the database
    product_data = [{"id": product.id, "name":product.name, "brand": product.brand, "price": product.price, "description": product.description} for prod in product]
    return jsonify(product_data)

#creating a new product to the database
@product.route('/Register', method=['POST'])
def register_products(): #creating a products
    data = request.json
    name = data.get("name")
    brand = data.get("brand")
    price = data.get("price")
    description = data.get("description")
    created_at = data.get("created_at")
    updated_at = data.get("updated_at")

    if not name or not brand or not price or not description:
        return jsonify({"error":"All fields are required"}), HTTP_400_BAD_REQUEST
    if Product.query.filter_by(name=name).first() is not None:
        return jsonify({"error":"The product is already registered"}), HTTP_409_CONFLICT
    
    try:
        new_product = Product(name=name, brand=brand, price=price, description=description)
        db.session.add(new_product) #adds a new product to the database
        db.session.commit()
        
        return jsonify({
            "message":new_product.name+"has been created"
        }), HTTP_201_CREATED
        
    except Exception as e:
        db.session.roolback()  
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR  
    
    
    
    # PUT to edit an existing product
@product.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    book = Product.query.get(id)
    if product is None:
        return jsonify({"message": "product not found"}), HTTP_404_NOT_FOUND
    data = request.json
    name = data.get("name")
    brand = data.get("brand")
    price = data.get("price")
    description = data.get("description")
    created_at = data.get("created_at")
    updated_at = data.get("updated_at") 
    
    db.session.commit()
    return jsonify({"message": "Product updated successfully", "product": {
        "id": product.id,
        "name": product.name,
        "brand": product.brand,
        "price": product.price,
        "description": product.description,
    }})
    
    # DELETE a product
@product.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id): #delete a book by id
    book = Product.query.get(id)
    if product is None:
        return jsonify({"message": "Product not found"}), HTTP_404_NOT_FOUND

    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}) 

    
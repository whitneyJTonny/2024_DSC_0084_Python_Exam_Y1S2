from flask import Flask
from app.models.category_model import Category
from flask import blueprints, request, jsonify #the blueprints are for verifying the product and jsonify for giving access to create a new product
from app.extensions import db
from app.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR

category = blueprints("/category", __name__,url_prefix_ = 'api/v1/category') #this is the endpoint


#creating a new category to the database
@category.route('/Register', method=['POST'])
def register_category(): #creating a category
    data = request.json
    name = data.get("name")
    expiry_date = data.get("expiry_date")
    description = data.get("description")
    created_at = data.get("created_at")
    updated_at = data.get("updated_at")

    if not name or not expiry_date  or not description:
        return jsonify({"error":"All fields are required"}), HTTP_400_BAD_REQUEST
    if Category.query.filter_by(name=name).first() is not None:
        return jsonify({"error":"The category is already registered"}), HTTP_409_CONFLICT
    
    try:
        new_category = Category(name=name, expiry_date=expiry_date, description=description)
        db.session.add(new_category) #adds a new category to the database
        db.session.commit()
        
        return jsonify({
            "message":new_category.name+"has been created"
        }), HTTP_201_CREATED
        
    except Exception as e:
        db.session.roolback()  
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR  
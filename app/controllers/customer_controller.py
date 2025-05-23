from flask import Flask
from app.models.customer_model import Customer
from flask import blueprints, request, jsonify #the blueprints are for verifying the product and jsonify for giving access to create a new product
from app.extensions import db
from app.status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_500_INTERNAL_SERVER_ERROR

customer = blueprints("/customer", __name__,url_prefix_ = 'api/v1/customer') #this is the endpoint


#creating a new category to the database
@customer.route('/Register', method=['POST'])
def register_customer(): #creating a customer
    data = request.json
    name = data.get("name")
    email = data.get("email")
    contact = data.get("contact")
    address = data.get("address")
    description = data.get("description")
    created_at = data.get("created_at")
    updated_at = data.get("updated_at")

    if not name or not email or not contact or not address  or not description:
        return jsonify({"error":"All fields are required"}), HTTP_400_BAD_REQUEST
    if Customer.query.filter_by(name=name).first() is not None:
        return jsonify({"error":"The customer is already registered"}), HTTP_409_CONFLICT
    
    try:
        new_customer = Customer(name=name, email=email,contact=contact,adress=address, description=description)
        db.session.add(new_customer) #adds a new customer to the database
        db.session.commit()
        
        return jsonify({
            "message":new_customer.name+"has been created"
        }), HTTP_201_CREATED
        
    except Exception as e:
        db.session.roolback()  
        return jsonify({"error": str(e)}), HTTP_500_INTERNAL_SERVER_ERROR  
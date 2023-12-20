from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

db = 'listings'

class Listings:
    def __init__(self, data):
        self.id=data['id']
        self.seller=data['seller']
        self.name=data['name']
        self.description=data['description']
        self.price=data['price']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def createListing(cls, data):
        valid=True
        if len(data['name']) < 3:
            flash("Name must be atleast 3 characters.")
            valid=False
        if len(data['description']) < 100 and len(data['description']) > 500:
            flash("desciption must be between 100 and 500 characters.")
            valid=False
        if not (data['price'] < 0):
            flash("Price must be greater than 0.")
            valid=False
        if valid:
            result=connectToMySQL(db).query_db("INSERT INTO listings (seller, name, desciption price) VALUES (%(seller)s, %(name)s, %(desciption)s, %(price)s)", data)
            print('_____________________________________________________')
            print(result)
            return valid
    
    @classmethod
    def get_all_listings_not_user(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM listings WHERE (id != %(id)s)", data)

    @classmethod
    def findListingByID(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM listings WHERE (id == %(id)s)", data)
    
    @classmethod
    def findListingBySeller(cls, data):
        return connectToMySQL(db).query_db("SELECT * FROM listings WHERE (seller == %(id)s)", data)

    @classmethod
    def updateListing(cls, data):
        valid=True
        if len(data['name']) < 3:
            flash("Name must be atleast 3 characters.")
            valid=False
        if len(data['description']) < 100 and len(data['description']) > 500:
            flash("desciption must be between 100 and 500 characters.")
            valid=False
        if not (data['price'] == 0):
            flash("Price must be greater than 0.")
            valid=False
        if valid:
            connectToMySQL(db).query_db("UPDATE listings SET name = %(name)s, description = %(description)s, price = %(price)s",data)
    
    @classmethod
    def deleteListing(cls,data):
        query = "DELETE FROM listings WHERE listings_id = %(seller_id)s;"
        result = connectToMySQL(db).query_db(query,data)
        return result
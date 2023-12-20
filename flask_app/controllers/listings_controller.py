from flask_app import app
from flask import render_template, redirect , request , session, flash
from flask_app.models.users_model import Users
from flask_app.models.listings_model import Listings

@app.route('/create_listings')
def create_listings():
    return render_template('create_listing.html')

@app.route('/...', methods=['POST'])
def create_listing_form():
    if not Listings_model.createListing(request.form):
        return redirect('/create_listings')
    data = { "name": request.form['name'],
            "description": request.form['descripton'],
            "price": request.form['price'],
            "seller_id": request.form['seller_id']
            }
    Listings_model.insertListing(data)
    return redirect('/create_listings')
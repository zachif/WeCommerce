from flask_app import app
from flask import render_template, redirect , request , session, flash , get_flashed_messages
from flask_app.models.user_model import User
from flask_app.models.listing_model import Listing

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
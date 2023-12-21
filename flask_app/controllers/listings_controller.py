from flask_app import app
from flask import render_template, redirect , request , session, flash
from flask_app.models.users_model import Users
from flask_app.models.listings_model import Listings

@app.route('/WeCommerce/your/listings')
def userListings():
    listings=Listings.findListingBySeller(session)
    for listing in listings:
        listing['price']=round(listing['price'],2)
    return render_template('user_listings.html', listings=listings)

@app.route('/WeCommerce/create')
def create_listings():
    return render_template('create_listing.html')

@app.route('/listing', methods=['POST'])
def create_listing_form():
    
    if request.form['price'] == "":
        request.form['price'] = 0
    print(request.form['price'])
    data = { 
        "name": request.form['name'],
        "description": request.form['description'],
        "price": float(request.form['price']),
        "seller": session['id']
    }
    valid = Listings.createListing(data)
    if not valid:
        return redirect('/WeCommerce/create')
    return redirect('/WeCommerce/your/listings')

@app.route('/edit/<int:id>')
def edit_listing(id):
    data = {
        'id' : id
    }
    return render_template('edit.html', listing = (Listings.findListingByID(data))[0])

@app.route('/WeCommerce/update/listing', methods =['POST'])
def update_listing_form():
    if request.form['price'] == "":
        request.form['price'] = 0
    data = {"name": request.form['name'],
            "description": request.form['descripton'],
            "price": float(request.form['price']),
            "seller": session['id']
            }
    valid = Listings.updateListing(data)
    if valid:
        return redirect('/WeCommerce/create')
    return redirect('/create_listing')

@app.route('/delete_listing')
def deleteListing(id):
    data = {
            "id": id
            }
    Listings.deleteListing(data)
    return redirect('/create_listing/'+ str(session['id']))

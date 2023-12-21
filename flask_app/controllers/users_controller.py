from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import Users
from flask_app.models.listings_model import Listings

@app.route('/WeCommerce')
def home():
    return render_template('login_reg.html')

@app.route("/register", methods=["POST"])
def register():
    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"]
    }
    print(data)
    valid=Users.register_user(data)
    
    print (valid)
    if not valid:
        return redirect('/WeCommerce')
    data['password']=request.form["password"]
    data['email']=request.form['email']
    current_user=Users.login_user(data)
    session['id']=current_user
    return redirect('/WeCommerce/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data={
        "email" : request.form["lemail"],
        "password" : request.form["lpassword"]
    }
    current_user=Users.login_user(data)
    if not current_user:
        return redirect('/WeCommerce')
    session['id']=current_user
    return redirect('/WeCommerce/dashboard')

@app.route('/WeCommerce/dashboard')
def dashboard():
    print(session['id'])
    user = Users.get_user_by_id(session)
    if not user:
        print(f"No user found for session ID: {session.get('id')}")
        return redirect('/WeCommerce')
    user = user[0]
    print(f"User data: {user}")
    listings=(Listings.get_all_listings_not_user(session))
    for listing in listings:
        listing['price']=round(listing['price'],2)
    return render_template('dash.html', user=(Users.get_user_by_id(session))[0], listings=listings)

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/WeCommerce')

#being nice
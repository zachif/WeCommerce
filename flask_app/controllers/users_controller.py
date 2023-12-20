from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import Users

@app.route('/WeCommerce')
def home():
    return render_template('index.html')

@app.route("/register", methods=["POST"])
def register():
    data ={
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "confirm_password" : request.form["confirm_password"]
    }
    valid=Users.register_user(data)
    print('_________________________________________________________')
    print (valid)
    if not valid:
        return redirect('/WeCommerce')
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



#being nice
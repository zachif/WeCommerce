from flask_app import app
from flask import render_template, redirect , request , session, flash
from flask_app.models.users_model import Users
from flask_app.models.listings_model import Listings
from flask_app.models.messages_model import Messages

@app.route('/WeCommerce/Messages/<int:correspondent>')
def message(correspondent):
    session['correspondent'] = correspondent
    data={
        'user' : session['id'],
        'corrispondant' : session['correspondent']
    }
    messages=Messages.retrieveMessagesByUsers(data)
    return render_template("message_user.html")
    
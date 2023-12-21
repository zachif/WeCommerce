from flask_app import app
from flask import render_template, redirect , request , session, flash
from flask_app.models.users_model import Users
from flask_app.models.listings_model import Listings
from flask_app.models.messages_model import Messages

@app.route('/WeCommerce/messages/<int:correspondent>')
def message(correspondent):
    session['correspondent'] = correspondent
    data={
        'user' : session['id'],
        'corrispondant' : session['correspondent']
    }
    messages=Messages.retrieveMessagesByUsers(data)
    print(messages)
    return render_template("message_user.html", messages=messages)
    
@app.route('/message', methods=['POST'])
def sendMessage():
    data={
        'content': request.form['message'],
        'sender' : session['id'],
        'recipiant' : session['correspondent']
    }
    Messages.sendMessage(data)
    return redirect('/WeCommerce/Messages/'+str(session['correspondent']))

@app.route('/WeCommerce/your/messages')
def yourMessages():
    return render_template("your_messages.html", corrispondants=Messages.getCorrispondantsByUser(session))
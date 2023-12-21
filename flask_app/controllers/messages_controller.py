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
    userData={
        "id":  session["id"]
    }
    correspondentData={
        "id": session['correspondent']
    }
    messages=Messages.retrieveMessagesByUsers(data)
    print(messages)
    return render_template("message_user.html", messages=messages, correspondent=session['correspondent'],sender=Users.get_user_by_id(userData),correspondentData=Users.get_user_by_id(correspondentData))
    
@app.route('/message', methods=['POST'])
def sendMessage():
    data={
        'content': request.form['message'],
        'sender' : session['id'],
        'recipiant' : session['correspondent']
    }
    Messages.sendMessage(data)
    return redirect('/WeCommerce/messages/'+str(session['correspondent']))

@app.route('/WeCommerce/your/messages')
def yourMessages():
    corrispondants=Messages.getCorrispondantsByUser(session)
    print(corrispondants)
    return render_template("your_messages.html", corrispondants=corrispondants)
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

db = 'listings'

class Messages:
    def __init__(self, data):
        self.id=data['id']
        self.sender=data['sender']
        self.recipiant=data['recipiant']
        self.content=data['content']  
        self.created_at=data['created_at']
        self.updated_at=data['update_at']

    @classmethod
    def sendMessage(cls, data):
        result=connectToMySQL(db).query_db("INSERT INTO messages (content, sender, recipiant) VALUES (%(content)s, %(sender)s, %(recipiant)s)", data)
        print(result)
        return result

    @classmethod
    def retrieveMessagesByUsers(cls, data):
        result=connectToMySQL(db).query_db("SELECT * FROM messages WHERE (sender = %(user)s OR sender = %(corrispondant)s) AND (recipiant = %(user)s OR recipiant = %(corrispondant)s)", data)
        print(result)
        return result
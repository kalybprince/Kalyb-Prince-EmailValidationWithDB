from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails ( email, created_at, updated_at ) VALUES ( %(email)s, NOW(), NOW() );"
        return connectToMySQL('email_db').query_db( query, data )

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_db').query_db( query )
        emails = []
        for email in results:
            emails.append( cls(email) )
        return email

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False
        else:
            flash("True", 'email')
            is_valid = True
        return is_valid
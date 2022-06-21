# # Model ---- CLASS AND @CLASSMETHODS

# # import the function that will return an instance of a connection
from dojos_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__( self , data ):
        self.id         = data['id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.age        = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# # ------------------ SAVE ONE NINJA ---------------------------
    @classmethod
    def save_ninja(cls, data):
        query = " INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s) ;"
        
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos').query_db(query, data)

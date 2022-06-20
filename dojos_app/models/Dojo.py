# Model ---- CLASS AND @CLASSMETHODS

# import the function that will return an instance of a connection
from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models import Ninja


class Dojo:
    def __init__( self , data ):
        self.id         = data['id']
        self.name       = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# ------------------ SHOW ALL DOJOS ---------------------------
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        
        # make sure to call the connectToMySQL function with the schema you are targeting.
        dojos_from_db = connectToMySQL('dojos').query_db(query)
        
        # Create an empty list to append our instances of dojos
        dojos = []

        # Iterate over the db results and create instances of dojos with cls.
        for dojo in dojos_from_db:
            dojos.append( cls(dojo) )
        return dojos


# ------------------ SHOW ONE DOJO WITH NINJAS---------------------------
    @classmethod
    #show one dojo with ninjas
    def show_dojo_ninjas(cls, data):
        query = " SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(dojos_id)s ;"  

        #result in a list
        results = connectToMySQL('dojos').query_db(query, data)

        dojos =  cls(results[0])


        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojos.ninja.append(Ninja.Ninja(ninja_data))
        return dojos

# ------------------ SAVE ONE DOJO ---------------------------
    @classmethod
    def save(cls, data):
        query = " INSERT INTO dojos (name, created_at, updated_at) VALUES( %(name)s, NOW(), NOW() ) ;" # make default values for created and updated at in MySqlbench
        
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos').query_db(query, data)




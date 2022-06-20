from flask import render_template, redirect, request
from dojos_app import app
from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models.Dojo import Dojo
from dojos_app.models import Ninja



# -----------------  SHOW ALL DOJOS: INDEX -------------------------
@app.route("/")
@app.route("/dojos")
def display_dojos():

    # return the get all classmethod to get all dojos 
    return render_template("new_dojo.html", dojos = Dojo.get_all())


# -----------------  SHOW ONE DOJO --------------------------------
@app.route('/dojos/show_dojo/<int:dojos_id>')
def show_dojo(dojos_id):
    data = {
        'dojos_id' : dojos_id
    }

    return render_template("show_dojo.html", dojo =  Dojo.show_dojo_ninjas(data))


# -----------------  CREATE NEW DOJO -------------------------
@app.route("/dojos/new_dojo")
def new_dojo():
    return render_template("new_dojo.html")


@app.route("/dojos/create_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }

    Dojo.save(data)

    return redirect('/dojos')
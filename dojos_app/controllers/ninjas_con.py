from flask import render_template, redirect, request
from dojos_app import app
from dojos_app.models.Ninja import Ninja
from dojos_app.models.Dojo import Dojo

# # ----------------- CREATE NEW NINJAS -------------------------------
@app.route("/new_ninja")
def new_ninja():
    return render_template("new_ninja.html", dojos = Dojo.get_all())


@app.route("/create_new_ninja", methods=["POST"])
def create_ninja():
    data = {
        "first_name"    : request.form["first_name"],
        "last_name"     : request.form["last_name"],
        "age"           : request.form["age"],
        "dojos_id"      : request.form["dojos_id"],
        "created_at"    : request.form["created_at"],
        "updated_at"    : request.form["updated_at"]
    }

    Ninja.save_ninja(data)

    return redirect('/dojos')


    # # ----------------- SHOW NINJAS PER DOJO -------------------------------




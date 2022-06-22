from crypt import methods
from flask import request, jsonify
from app import app, db
from app import User

@app.route("/user/list", methods = ["GET"])
def user_list():
    users = User.query.all()
    arr = []
    
    for user in users:
        arr.append(user.to_dict())
   
    return jsonify({"elements": arr, "error": False})

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/soma/<int:n1>/<int:n2>/numero")
def soma(n1, n2):
    return "Hello World! {} - {}".format(n1, n2)

@app.route("/user/add", methods = ["POST"])
def user_add():
    data = request.get_json()
    
    if "username" not in data or data["username"] is None:
        return jsonify({"error": True,"message": "O username nao foi informado."}), 400

    if "email" not in data or data["email"] is None:
        return jsonify({"error": True,"message": "O username nao foi informado."}), 400

    
    user = User()
    user.username = data["username"]
    user.email = data["email"]
    
    try:  
        db.session.add(user)
        db.session.commit()
        return jsonify({"error": False})
    
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "O username ou email a existe!"})
    
@app.route("/user/delete/<int:id>", methods = ["DELETE"])
def user_delete(id):
    
    user = User.query.get(id)
   
    if user == None:
         return jsonify({"error": True, "message": "Usuario foi deletado."}), 404
     
    db.session.delete(user)
    
    try:  
        db.session.commit()
        return jsonify({"message": "Usuario nao existe.", "error": False}), 200

       
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "erro ao deletar."}), 200


@app.route("/user/edit/<int:id>", methods = ["PUT"])
def user_edit(id):
    data = request.get_json()
    
    user = User.query.get(id)
    user.username = data["novo_username"]
    user.email = data["novo_email"]
    try:  
        db.session.commit()
        return jsonify({ "error": False, "message": "Usuario nao existe."}), 200

       
    except:
        db.session.rollback()
        
        return jsonify({"error": True, "message": "erro ao deletar."}), 400

        
@app.route("/user/view/<int:id>", methods = ["GET"])
def user_view(id):
    
    user = User.query.get(id)
   
    if user == None:
         return jsonify({"message": "Usuario nao existe.", "error": True}), 404
     
    return jsonify(
        {
            "data": user.to_dict(),
            "error": False
        }
    )
        
    
    
    
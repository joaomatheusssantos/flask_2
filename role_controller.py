from app import app, db
from flask import request, jsonify
from app import Role

@app.route("/role/list",methods=["GET"])
def list_role():
    roles = Role.query.all()
    arr = []
    
    for role in roles:
        arr.append(role.to_dict())

    return jsonify({"elements": arr, "error": False})

@app.route("/role/add",methods=["POST"])
def add_role():
    data = request.get_json()

    if "nome" not in data or data["nome"] is None:
        return jsonify ({"Error":True, "Message": "nome não foi informado"}), 400
    
    role = Role()
    role.nome = data["nome"]
    try:
        db.session.add(role)
        db.session.commit()
        return jsonify ({"error": False})

    except:
        db.session.rollback()
        return jsonify({"Error":True, "Mensagem": "Role ja existente"})

@app.route("/role/delete/<int:id>",methods=["DELETE"])
def delete_role(id):
    role = Role.query.get(id)
    
    if role == None:
        return jsonify({"message": "O role não existe", "error":True}), 404
    
    db.session.delete(role)

    try:
        db.session.commit()
        return jsonify({"message": "Role deletado", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel role o usuario", "error":False}), 200

@app.route("/role/edit/<int:id>",methods=["PUT"])
def edit_role(id):
    role = Role.query.get(id)
    data = request.get_json()

    if role == None:
        return jsonify({"message": "O usuario não existe", "error":True}), 404
    
    try:
        if "nome" in data:
            role.nome = data["nome"]

        db.session.commit()
        return jsonify({"message": "Role editado", "error":False}), 200
    except:
        db.session.rollback()
        return jsonify({"message": "Não foi possivel editar role", "error":True}), 200

@app.route("/role/view/<int:id>",methods=["GET"])
def view_role(id):
    role = Role.query.get(id)

    if role == None:
        return jsonify({"message": "O role não existe", "error":True}), 404
    
    return jsonify({
        "data": role.to_dict(),
        "error": False
    })

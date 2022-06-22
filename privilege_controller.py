from flask import request, jsonify
from app import app, db
from app import Privilege
       
@app.route("/privilege/list", methods = ["GET"])
def privilege_list():
    privileges = Privilege.query.all()
    arr = []
    
    for privilege in privileges:
        arr.append(privilege.to_dict())
   
    return jsonify({"elements": arr, "error": False})

@app.route("/privilege/add", methods = ["POST"])
def privilege_add():
    data = request.get_json()
    
    if "role_id" not in data or data["role_id"] is None:
        return jsonify({"error": True,"message": "Role_id não foi informado."}), 400

    if "resource_id" not in data or data["resource_id"] is None:
        return jsonify({"error": True,"message": "Resource_id não foi informado."}), 400
     
    if "allow" not in data or data["allow"] is None:
        return jsonify({"error": True,"message": "Allow não foi informado."}), 400

    
    privilege = Privilege(role_id = data["role_id"], resource_id = data["resource_id"], allow= data["allow"])
    
    try:  
        db.session.add(privilege)
        db.session.commit()
        return jsonify({"error": False})
    
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Não foi possivel cadastrar privilegio."})
    
@app.route("/privilege/delete/<int:resource_id>&<int:role_id>", methods = ["DELETE"])
def privilege_delete(resource_id, role_id):
    
    privilege = Privilege.query.filter(resource_id==resource_id, role_id==role_id).first()
   
    if privilege == None:
         return jsonify({"error": True, "message": "O usuário não existe."}), 404
           
    db.session.delete(privilege)
    
    try:  
        db.session.commit()
        return jsonify({"message": "O usuário sumiu.", "error": False}), 200

       
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar."}), 200


@app.route("/privilege/edit/<int:role_id>&<int:resource_id>", methods = ["PUT"])
def privilege_edit(role_id, resource_id):
    privilege = Privilege.query.filter(role_id==role_id, resource_id==resource_id).first()
    data = request.get_json()
    
    try:  
        privilege.role_id = data["role_id"]
        privilege.resource_id = data["resource_id"]
        privilege.allow = data["allow"]
  
        db.session.commit()
        return jsonify({ "error": False, "message": "O Privilegio foi mudado."}), 200

       
    except:
        db.session.rollback()
        
        return jsonify({"error": True, "message": "Erro ao editar."}), 400

@app.route("/privilege/view/<int:resource_id>&<int:role_id>", methods = ["GET"]) 
def privilege_view(resource_id, role_id): 
    
    privilege = Privilege.query.filter(resource_id==resource_id, role_id==role_id).first()
    
    if privilege == None: 
        return jsonify({"message": "Privilege não existe.", "error": True}), 404 
    
    return jsonify( 
        { 
            "data": privilege.to_dict(), 
            "error": False 
        } 
    )
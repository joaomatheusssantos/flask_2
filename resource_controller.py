from flask import request, jsonify
from app import app, db
from app import Resource
       
@app.route("/resource/list", methods = ["GET"])
def resource_list():
    resources = Resource.query.all()
    arr = []
    
    for resource in resources:
        arr.append(resource.to_dict())
   
    return jsonify({"elements": arr, "error": False})

@app.route("/resource/add", methods = ["POST"])
def resource_add():
    data = request.get_json()

    if "action_id" not in data or data["action_id"] is None:
        return jsonify({"error": True,"message": "Resource_id não foi informado."}), 400
     
    if "controller_id" not in data or data["controller_id"] is None:
        return jsonify({"error": True,"message": "controller_id não foi informado."}), 400

    
    resource = Resource()
    resource.action_id = data["action_id"]
    resource.controller_id = data["controller_id"]
    
    try:  
        db.session.add(resource)
        db.session.commit()
        return jsonify({"error": False})
    
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "O resource já existe!"})
    
@app.route("/resource/delete/<int:id>", methods = ["DELETE"])
def resource_delete(id):
    
    resource = Resource.query.get(id)
   
    if resource == None:
         return jsonify({"error": True, "message": "Resource foi deletado."}), 404
           
    db.session.delete(resource)
    
    try:  
        db.session.commit()
        return jsonify({"message": "Resource não existe.", "error": False}), 200

       
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar."}), 200


@app.route("/resource/edit/<int:id>", methods = ["PUT"])
def resource_edit(id):
    data = request.get_json()
    
    resource = Resource.query.get(id)
    
    if resource == None: 
        return jsonify({"message": "Resource não existe.", "error": True}), 404 
    
    
    resource.action_id = data["action_id"]
    resource.controller_id = data["controller_id"]
   
    try:  
        db.session.commit()
        return jsonify({ "error": False, "message": "O resource não existe."}), 200

       
    except:
        db.session.rollback()
        
        return jsonify({"error": True, "message": "Erro."}), 400

@app.route("/resource/view/<int:id>", methods = ["GET"]) 
def resource_view(id): 
    
    resource = Resource.query.get(id) 
    
    if resource == None: 
        return jsonify({"message": "Resource não existe.", "error": True}), 404 
    
    return jsonify( 
        { 
            "data": resource.to_dict(), 
            "error": False 
        } 
    )
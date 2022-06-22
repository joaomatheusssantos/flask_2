from flask import request, jsonify
from app import app, db
from app import Action
       
@app.route("/action/list", methods = ["GET"])
def action_list():
    actions = Action.query.all()
    arr = []
    
    for action in actions:
        arr.append(action.to_dict())
   
    return jsonify({"elements": arr, "error": False})

@app.route("/action/add", methods = ["POST"])
def action_add():
    data = request.get_json()


    if "nome" not in data or data["nome"] is None:
        return jsonify({"error": True,"message": "Nome não foi informado."}), 400
     
    action = Action()
    action.nome = data["nome"]
    
    try:  
        db.session.add(action)
        db.session.commit()
        return jsonify({"error": False})
    
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Usuário já existe!"})
    
@app.route("/action/delete/<int:id>", methods = ["DELETE"])
def action_delete(id):
    
    action = Action.query.get(id)
   
    if action == None:
         return jsonify({"error": True, "message": "O usuário foi deletado."}), 404
           
    db.session.delete(action)
    
    try:  
        db.session.commit()
        return jsonify({"message": " apagadoo.", "error": False}), 200

       
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar."}), 200


@app.route("/action/edit/<int:id>", methods = ["PUT"])
def action_edit(id):
    data = request.get_json()
    
    action = Action.query.get(id)
    action.nome = data["novo_nome"]
   
    try:  
        db.session.commit()
        return jsonify({ "error": False, "message": "Deu bom."}), 200

       
    except:
        db.session.rollback()
        
        return jsonify({"error": True, "message": "Erro ao deletar."}), 400

@app.route("/action/view/<int:id>", methods = ["GET"]) 
def action_view(id): 
    
    action = Action.query.get(id) 
    
    if action == None: 
        return jsonify({"message": "Action não existe.", "error": True}), 404 
    
    return jsonify( 
        { 
            "data": action.to_dict(), 
            "error": False 
        } 
    )
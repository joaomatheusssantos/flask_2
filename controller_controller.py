from flask import request, jsonify
from app import app, db
from app import Controller
       
@app.route("/controller/list", methods = ["GET"])
def controller_list():
    controllers = Controller.query.all()
    arr = []
    
    for controller in controllers:
        arr.append(controller.to_dict())
   
    return jsonify({"elements": arr, "error": False})

@app.route("/controller/add", methods = ["POST"])
def controller_add():
    data = request.get_json()
    
    if "nome" not in data or data["nome"] is None:
        return jsonify({"error": True,"message": "Nome não foi informado."}), 400
     
    controller = Controller()
    controller.nome = data["nome"]
    
    try:  
        db.session.add(controller)
        db.session.commit()
        return jsonify({"error": False})
    
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Usuário já existe!"})
    
@app.route("/controller/delete/<int:id>", methods = ["DELETE"])
def controller_delete(id):
    
    controller = Controller.query.get(id)
   
    if controller == None:
         return jsonify({"error": True, "message": "O usuário foi deletado."}), 404
           
    db.session.delete(controller)
    
    try:  
        db.session.commit()
        return jsonify({"message": "apagadu.", "error": False}), 200

       
    except:
        db.session.rollback()
        return jsonify({"error": True, "message": "Erro ao deletar."}), 200


@app.route("/controller/edit/<int:id>", methods = ["PUT"])
def controller_edit(id):
    data = request.get_json()
    
    controller = Controller.query.get(id)
    controller.nome = data["novo_nome"]
   
    try:  
        db.session.commit()
        return jsonify({ "error": False, "message": "O usuário não existe."}), 200

       
    except:
        db.session.rollback()
        
        return jsonify({"error": True, "message": "Erro ao deletar."}), 400

@app.route("/controller/view/<int:id>", methods = ["GET"]) 
def controller_view(id): 
    
    controller = Controller.query.get(id) 
    
    if controller == None: 
        return jsonify({"message": "Controller não existe.", "error": True}), 404 
    
    return jsonify( 
        { 
            "data": controller.to_dict(), 
            "error": False 
        } 
    )
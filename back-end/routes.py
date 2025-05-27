from app import app, db
from flask import request, jsonify
from models import Pets

# 获取所有宠物
@app.route("/api/pets", methods=["GET"])
def get_pets():
    pets = Pets.query.all()
    result = [pet.to_json() for pet in pets]  # ✅ 修改 pets.to_json → pet.to_json
    return jsonify(result)

# 新增一个宠物
@app.route("/api/pets", methods=["POST"])

def create_pet():
    try:
        data = request.json

        required_fields = ["name","breed","description","gender"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error":f'missing some required parts:{field}'}), 400

        name = data.get("name")
        breed = data.get("breed")
        description = data.get("description")
        gender = data.get("gender")
        
        #fetch avatar image based on gender
        # 但是我后面想要修改这个部分--主人/宠物的部分。所以后面开发完过后再改吧

        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":                
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None
        #这里的f是fetch的意思

        new_pets = Pets(name=name, breed=breed, description=description, gender=gender, img_url=img_url)

        # like github, add+commit+show message
        db.session.add(new_pets)
        db.session.commit()
        return jsonify({"msg":"A new lovely pet created successfully"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    # this is the exception state, which in case sth wrong happened

#try to delete a pet by myself:
@app.route("/api/pets/<int:id>", methods=["DELETE"])

def delete_pet(id):
    try:
        #首先拿到id
        pet = Pets.query.get(id)
        #如果没有这个id
        if pet is None:
            return jsonify({"error":"no this pet!"}),404
        
        db.session.delete(pet)
        db.session.commit()
        return jsonify({"msg":"deleted already!"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500

#update a pet
@app.route("/api/pets/<int:id>",methods=["PATCH"])
def update_pet(id):
  try:
    pet = Pets.query.get(id)
    if pet is None:
      return jsonify({"error":"pet not found"}), 404
    
    data = request.json

    pet.name = data.get("name",pet.name)
    pet.description = data.get("description",pet.description)
    pet.gender = data.get("gender",pet.gender)
    pet.breed = data.get("breed",pet.breed)

    db.session.commit()
    return jsonify(pet.to_json()),200
  
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}),500

    #test: localhost:5000/api/pet
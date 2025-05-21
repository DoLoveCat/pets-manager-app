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

def create_friend():
    try:
        data = request.json

        name = data.get("name")
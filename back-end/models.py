# store database schema （数据库架构） in the models.py file
# a table in our database

from app import db

class Pets(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  breed = db.Column(db.String(50), nullable=False)
  description = db.Column(db.Text, nullable=False)
  gender = db.Column(db.String(10), nullable=False)
  img_url = db.Column(db.String(200), nullable=True)
#nullable=False：字段必须填写
#nullable=True：字段可以留空

  def to_json(self):
    return {
      "id":self.id,
      "name":self.name,
      "breed":self.breed,
      "description":self.description,
      "gender":self.gender,
      "imgUrl":self.img_url,
      #左边python写法，右边js写法
    }
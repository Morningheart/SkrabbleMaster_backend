from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import db


class CarModel(db.Model):
	__tablename__ = 'cars'
	id = Column(Integer(), primary_key=True)

	ingame_id = Column(String(255), nullable=False)

	model = Column(String(255), nullable=False)

	brand_name = Column(String(255), nullable=False)
	setups = relationship('SetupModel', lazy="dynamic" , primaryjoin="CarModel.id == SetupModel.car_id")

	def __init__(self, ingame_id, brand_name, model):
		self.ingame_id = ingame_id
		self.brand_name = brand_name
		self.model = model

	def __repr__(self):
		return f"<Car {self.id}>"

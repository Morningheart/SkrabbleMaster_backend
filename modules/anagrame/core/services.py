from .models import CarModel
from ..adapters.sqlachemy import SQLACarAdapter

adapter = SQLACarAdapter()


class CarService:
	def get_cars(self) -> list[CarModel]:
		return adapter.get_cars()

	def get_car(self, id):
		return adapter.get_car(id)

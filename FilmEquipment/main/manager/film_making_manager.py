import doctest
from typing import List

from main.model.shooting_equipment import ShootingEquipment
from main.model.camera import Camera
from main.model.costume import Costume


class FilmMakingManager:

    def __init__(self):
        self.equipment: List[ShootingEquipment] = []
        self.costumes: List[Costume] = []

    def add_items(self, items: List[ShootingEquipment]):
        self.equipment.extend(items)

    def add_item(self, item: ShootingEquipment):
        self.equipment.append(item)

    def add_costumes(self, costumes: List[Costume]):
        self.costumes.extend(costumes)

    def add_costume(self, costume: Costume):
        self.costumes.append(costume)

    def find_equipment_with_warranty_period_greater_than(self, warranty_work_period_in_months: int):
        """
        Returns objects with warranty period greater than 3 months
        >>> equipment_for_test: List[ShootingEquipment] = [Costume(warranty_work_period_in_months=12), Camera(warranty_work_period_in_months=6), Camera(warranty_work_period_in_months=1)]
        >>> film_making_manager = FilmMakingManager()
        >>> film_making_manager.add_items(equipment_for_test)
        >>> result_equipment: List[ShootingEquipment] = film_making_manager.find_equipment_with_warranty_period_greater_than(3)
        >>> [item.warranty_work_period_in_months for item in result_equipment]
        [12, 6]
        """
        result: List[ShootingEquipment] = []
        for equipment in self.equipment:
            if equipment.warranty_work_period_in_months > warranty_work_period_in_months:
                result.append(equipment)
        return result

    def find_costumes_for_historical_film(self, category: str, year_of_use: int):
        """
        Return list of objects if object`s category = Historical or year_of_use < 1991
        >>> costumes_for_test: List[Costume] = [Costume(production_year=2010, year_of_use=1992, category="Historical"), Costume(production_year=2004, year_of_use=1995, category="Western"), Costume(production_year=2016, year_of_use=1914, category="Drama")]
        >>> film_making_manager = FilmMakingManager()
        >>> film_making_manager.add_costumes(costumes_for_test)
        >>> result_costumes: List[Costume] = film_making_manager.find_costumes_for_historical_film("Historical", 1991)

        Second object in first result list has year_of_use less than 1991 but also has category Drama,

        >>> [costume.category for costume in result_costumes]
        ['Historical', 'Drama']

        First object in second result list has category Historical but also has year_of_use greater than 1991, so it is in the list

        >>> [costume.year_of_use for costume in result_costumes]
        [1992, 1914]
        """
        result: List[Costume] = []
        for film_wear in self.costumes:
            if film_wear.category == category:
                result.append(film_wear)
            if film_wear.year_of_use < year_of_use:
                result.append(film_wear)
        return result


if __name__ == "__main__":
    doctest.testmod()


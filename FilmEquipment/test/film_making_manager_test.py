import unittest
from typing import List

from main.manager.film_making_manager import FilmMakingManager
from main.model.abstract_shooting_equipment import AbstractShootingEquipment
from main.model.costume import Costume
from .base_film_making_manager_test import BaseFilmMakingManagerTest


class FilmMakingManagerTest(BaseFilmMakingManagerTest, unittest.TestCase):

    def setUp(self):
        self.film_making_manager = FilmMakingManager()
        self.film_making_manager.add_costumes(self.costumes)
        self.film_making_manager.add_items(self.equipment)

    def test_find_equipment_with_warranty_period_greater_than(self):
        result_equipment: List[
            AbstractShootingEquipment] = self.film_making_manager.find_equipment_with_warranty_period_greater_than(3)
        self.assertTrue(len(result_equipment) >= 1)
        for item in result_equipment:
            self.assertTrue(item.warranty_work_period_in_months > 3)

    def test_find_costumes_for_historical_film(self):
        result_costumes: List[Costume] = self.film_making_manager.find_costumes_for_historical_film("Historical", 1991)
        self.assertTrue(len(result_costumes) >= 1)
        for costume in result_costumes:
            self.assertTrue(costume.category == "Historical" or costume.year_of_use < 1991)

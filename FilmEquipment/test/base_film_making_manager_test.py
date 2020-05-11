import unittest
from abc import ABC
from typing import List

from main.model.shooting_equipment import ShootingEquipment
from main.model.camera import Camera
from main.model.costume import Costume


class BaseFilmMakingManagerTest(ABC, unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.costumes: List[Costume] = []
        self.equipment: List[ShootingEquipment] = []

    def setUp(self):
        self.costumes.append(Costume(production_year=2016, year_of_use=1914, category="Drama"))
        self.costumes.append(Costume(production_year=2004, year_of_use=1995, category="Western"))
        self.costumes.append(Costume(production_year=2010, year_of_use=1992, category="Historical"))
        self.equipment.append(Costume(warranty_work_period_in_months=12))
        self.equipment.append(Camera(warranty_work_period_in_months=6))
        self.equipment.append(Camera(warranty_work_period_in_months=1))

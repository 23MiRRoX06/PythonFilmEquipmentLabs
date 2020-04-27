import unittest

from main.manager.film_making_manager_utils import FilmMakingManagerUtils
from main.model.sort_type import SortType
from .base_film_making_manager_test import BaseFilmMakingManagerTest


class FilmMakingManagerUtilsTest(BaseFilmMakingManagerTest, unittest.TestCase):

    def test_sort_costumes_by_year_of_use_ascending(self):
        FilmMakingManagerUtils.sort_costumes_by_year_of_use(self.costumes, SortType.ASC)
        for costumeIndex in range(len(self.costumes) - 1):
            self.assertTrue(self.costumes[costumeIndex].year_of_use < self.costumes[1 + costumeIndex].year_of_use)

    def test_sort_costumes_by_year_of_use_descending(self):
        FilmMakingManagerUtils.sort_costumes_by_year_of_use(self.costumes, SortType.DESC)
        for costumeIndex in range(len(self.costumes) - 1):
            self.assertTrue(self.costumes[costumeIndex].year_of_use > self.costumes[1 + costumeIndex].year_of_use)

    def test_sort_costumes_by_production_year_ascending(self):
        FilmMakingManagerUtils.sort_costumes_by_production_year(self.costumes, SortType.ASC)
        for costumeIndex in range(len(self.costumes) - 1):
            self.assertTrue(
                self.costumes[costumeIndex].production_year < self.costumes[1 + costumeIndex].production_year)

    def test_sort_costumes_by_production_year_descending(self):
        FilmMakingManagerUtils.sort_costumes_by_production_year(self.costumes, SortType.DESC)
        for costumeIndex in range(len(self.costumes) - 1):
            self.assertTrue(
                self.costumes[costumeIndex].production_year > self.costumes[1 + costumeIndex].production_year)

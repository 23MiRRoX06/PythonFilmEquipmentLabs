import doctest
from typing import List

from main.model.costume import Costume
from main.model.sort_type import SortType


class FilmMakingManagerUtils:

    @staticmethod
    def sort_costumes_by_year_of_use(costumes: List[Costume], sort_type: SortType):
        """
        Test sorting by year_of_use ascending
        >>> costumes_for_test: List[Costume] = [Costume(production_year=2010, year_of_use=1992, category="Historical"), Costume(production_year=2004, year_of_use=1995, category="Western"), Costume(production_year=2016, year_of_use=1914, category="Drama")]
        >>> FilmMakingManagerUtils.sort_costumes_by_year_of_use(costumes_for_test, SortType.ASC)
        >>> [costume.year_of_use for costume in costumes_for_test]
        [1914, 1992, 1995]

        Test sorting by year_of_use descending

         >>> FilmMakingManagerUtils.sort_costumes_by_year_of_use(costumes_for_test, SortType.DESC)
         >>> [costume.year_of_use for costume in costumes_for_test]
         [1995, 1992, 1914]
        """
        if sort_type == SortType.ASC:
            costumes.sort(key=lambda costume: costume.year_of_use)
        else:
            costumes.sort(key=lambda costume: costume.year_of_use, reverse=True)

    @staticmethod
    def sort_costumes_by_production_year(costumes: List[Costume], sort_type: SortType):
        """
        Test sorting by production_year ascending

        >>> costumes_for_test: List[Costume] = [Costume(production_year=2010, year_of_use=1992, category="Historical"), Costume(production_year=2004, year_of_use=1995, category="Western"), Costume(production_year=2016, year_of_use=1914, category="Drama")]
        >>> FilmMakingManagerUtils.sort_costumes_by_production_year(costumes_for_test, SortType.ASC)
        >>> [costume.production_year for costume in costumes_for_test]
        [2004, 2010, 2016]

        Test sorting by year_of_use descending

        >>> FilmMakingManagerUtils.sort_costumes_by_production_year(costumes_for_test, SortType.DESC)
        >>> [costume.production_year for costume in costumes_for_test]
        [2016, 2010, 2004]
        """
        if sort_type == SortType.ASC:
            costumes.sort(key=lambda costume: costume.production_year)
        else:
            costumes.sort(key=lambda costume: costume.production_year, reverse=True)


if __name__ == "__main__":
    doctest.testmod()

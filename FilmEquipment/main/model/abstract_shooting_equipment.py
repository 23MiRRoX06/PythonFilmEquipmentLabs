from abc import ABC


class AbstractShootingEquipment(ABC):
    def __init__(self, production_year, warranty_work_period_in_months, factory_manufacturer, country_manufacturer,
                 model_name, material, weight_in_grams, color):
        self.production_year = production_year
        self.warranty_work_period_in_months = warranty_work_period_in_months
        self.factory_manufacturer = factory_manufacturer
        self.model_name = model_name
        self.material = material
        self.weight_in_grams = weight_in_grams
        self.color = color

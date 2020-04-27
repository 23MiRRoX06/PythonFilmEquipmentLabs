from abc import ABC

from main.model.abstract_shooting_equipment import AbstractShootingEquipment


class AbstractRecordingDevice(AbstractShootingEquipment, ABC):
    def __init__(self, is_waterproof, battery_life_in_hours, record_format, production_year,
                 warranty_work_period_in_months, factory_manufacturer, country_manufacturer, model_name, material,
                 weight_in_grams, color):
        super().__init__(production_year, warranty_work_period_in_months, factory_manufacturer, country_manufacturer,
                         model_name, material, weight_in_grams, color)
        self.is_waterproof = is_waterproof
        self.battery_life_in_hours = battery_life_in_hours
        self.record_format = record_format

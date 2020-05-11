from main.model.quality import Quality
from main.model.shooting_equipment import ShootingEquipment


class Costume(ShootingEquipment):
    def __init__(self, year_of_use=1712, category="Christmas", size_eur="M", fabric_quality=Quality.MIDDLE,
                 components="Pants and shirt", production_year=2010, warranty_work_period_in_months=12,
                 factory_manufacturer="personage.ua", country_manufacturer="Ukraine", model_name="Santa",
                 material="fabric", weight_in_grams=7000, color="red"):
        super().__init__(production_year, warranty_work_period_in_months, factory_manufacturer, country_manufacturer,
                         model_name, material, weight_in_grams, color)
        self.year_of_use = year_of_use
        self.category = category
        self.size_eur = size_eur
        self.fabric_quality = fabric_quality
        self.components = components

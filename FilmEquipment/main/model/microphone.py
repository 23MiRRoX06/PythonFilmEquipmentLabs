from main.model.recording_device import RecordingDevice


class Microphone(RecordingDevice):
    def __init__(self, frequency_range_in_hz, dynamic_range_in_db, is_windproof, mount_type, is_waterproof,
                 battery_life_in_hours, record_format, production_year, warranty_work_period_in_months,
                 factory_manufacturer, country_manufacturer, model_name, material, weight_in_grams, color):
        super().__init__(is_waterproof, battery_life_in_hours, record_format, production_year,
                         warranty_work_period_in_months, factory_manufacturer, country_manufacturer, model_name,
                         material, weight_in_grams, color)
        self.frequency_range_in_hz = frequency_range_in_hz
        self.dynamic_range_in_db = dynamic_range_in_db
        self.is_windproof = is_windproof
        self.mount_type = mount_type

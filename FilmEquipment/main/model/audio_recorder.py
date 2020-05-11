from main.model.recording_device import RecordingDevice


class AudioRecorder(RecordingDevice):
    def __init__(self, recording_channels_number, recording_duration_in_minutes, is_waterproof, battery_life_in_hours,
                 record_format, production_year, warranty_work_period_in_months, factory_manufacturer,
                 country_manufacturer, model_name, material, weight_in_grams, color):
        super().__init__(is_waterproof, battery_life_in_hours, record_format, production_year,
                         warranty_work_period_in_months, factory_manufacturer, country_manufacturer, model_name,
                         material, weight_in_grams, color)
        self.recording_channels_number = recording_channels_number
        self.recording_duration_in_minutes = recording_duration_in_minutes

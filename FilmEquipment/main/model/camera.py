from main.model.recording_device import RecordingDevice


class Camera(RecordingDevice):
    def __init__(self, video_resolution_standart="4K", video_fraps_per_second=120, video_recording_speed_in_mbps=150,
                 viewing_angle_in_degrees=55, has_lcd_monitor=True, is_waterproof=True, battery_life_in_hours=12,
                 record_format="mp4", production_year=2017, warranty_work_period_in_months=24,
                 factory_manufacturer="Canon", country_manufacturer="China",
                 model_name="MSP-345", material="plastic", weight_in_grams=420, color="black"):
        super().__init__(is_waterproof, battery_life_in_hours, record_format, production_year,
                         warranty_work_period_in_months, factory_manufacturer, country_manufacturer, model_name,
                         material, weight_in_grams, color)
        self.video_resolution_standart = video_resolution_standart
        self.video_fraps_per_second = video_fraps_per_second
        self.video_recording_speed_in_mbps = video_recording_speed_in_mbps
        self.viewing_angle_in_degrees = viewing_angle_in_degrees
        self.has_lcd_monitor = has_lcd_monitor

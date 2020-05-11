from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from main.model.microphone import Microphone

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://OstapIoT2019:528193746@localhost:3306/pythonFilmEquipment"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class UpdatedMicrophone(Microphone, db.Model):
    __tablename__ = "Microphone"
    id = db.Column(db.Integer, primary_key=True)
    connection_type = db.Column(db.String(20), unique=False)
    frequency_range_in_hz = db.Column(db.Integer, unique=False)
    dynamic_range_in_db = db.Column(db.Integer, unique=False)
    is_windproof = db.Column(db.Boolean, unique=False)
    mount_type = db.Column(db.String(20), unique=False)
    is_waterproof = db.Column(db.Boolean, unique=False)
    battery_life_in_hours = db.Column(db.Integer, unique=False)
    record_format = db.Column(db.String(10), unique=False)
    production_year = db.Column(db.Integer, unique=False)
    warranty_work_period_in_months = db.Column(db.Integer, unique=False)
    factory_manufacturer = db.Column(db.String(20), unique=False)
    country_manufacturer = db.Column(db.String(60), unique=False)
    model_name = db.Column(db.String(20), unique=False)
    material = db.Column(db.String(10), unique=False)
    weight_in_grams = db.Column(db.Integer, unique=False)
    color = db.Column(db.String(40), unique=False)

    def __init__(self, connection_type, frequency_range_in_hz, dynamic_range_in_db, is_windproof, mount_type,
                 is_waterproof,
                 battery_life_in_hours, record_format, production_year, warranty_work_period_in_months,
                 factory_manufacturer, country_manufacturer, model_name, material, weight_in_grams, color):
        super().__init__(frequency_range_in_hz, dynamic_range_in_db, is_windproof, mount_type, is_waterproof,
                         battery_life_in_hours, record_format, production_year, warranty_work_period_in_months,
                         factory_manufacturer, country_manufacturer, model_name, material, weight_in_grams, color)
        self.connection_type = connection_type


class MicrophoneSchema(ma.Schema):
    class Meta:
        fields = ("production_year", "country_manufacturer", "record_format")


microphone_schema = MicrophoneSchema()
microphones_schema = MicrophoneSchema(many=True)


@app.route("/microphone", methods=["POST"])
def add_microphone():
    connection_type = request.json["connection_type"]
    frequency_range_in_hz = request.json["frequency_range_in_hz"]
    dynamic_range_in_db = request.json["dynamic_range_in_db"]
    mount_type = request.json["mount_type"]
    battery_life_in_hours = request.json["battery_life_in_hours"]
    record_format = request.json["record_format"]
    production_year = request.json["production_year"]
    warranty_work_period_in_months = request.json["warranty_work_period_in_months"]
    factory_manufacturer = request.json["factory_manufacturer"]
    country_manufacturer = request.json["country_manufacturer"]
    model_name = request.json["model_name"]
    material = request.json["material"]
    weight_in_grams = request.json["weight_in_grams"]
    color = request.json["color"]
    microphone = UpdatedMicrophone(connection_type, frequency_range_in_hz, dynamic_range_in_db, True,
                                   mount_type, True, battery_life_in_hours, record_format, production_year,
                                   warranty_work_period_in_months, factory_manufacturer, country_manufacturer,
                                   model_name, material, weight_in_grams, color)
    db.session.add(microphone)
    db.session.commit()

    return jsonify(microphone)


@app.route("/microphone", methods=["GET"])
def get_all_microphones():
    all_microphones = UpdatedMicrophone.query.all()
    result = microphones_schema.dump(all_microphones)
    return jsonify(result.data)


@app.route("/microphone/<id>", methods=["GET"])
def get_microphone(id):
    microphone = UpdatedMicrophone.query.get(id)
    return microphone_schema.jsonify(microphone)


@app.route("/microphone/<id>", methods=["DELETE"])
def delete_microphone(id):
    microphone = UpdatedMicrophone.query.get(id)
    db.session.delete(microphone)
    db.session.commit()
    return microphone_schema.jsonify(microphone)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

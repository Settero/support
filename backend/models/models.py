from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()


def generate_uuid():
    return str(uuid.uuid4())


# 🔷 Building
class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # связи
    rooms = db.relationship('Room', backref='building', lazy=True)


# 🔷 Room
class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    building_id = db.Column(db.String(36), db.ForeignKey('building.id'), nullable=False)

    name = db.Column(db.String(255), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    area = db.Column(db.Float, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # связи
    devices = db.relationship('Device', backref='room', lazy=True)


# 🔷 Unit
class Unit(db.Model):
    __tablename__ = 'unit'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)

    name = db.Column(db.String(50), nullable=False, unique=True)
    symbol = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    # связи
    device_types = db.relationship('DeviceType', backref='default_unit', lazy=True)
    telemetry = db.relationship('Telemetry', backref='unit', lazy=True)


# 🔷 DeviceType
class DeviceType(db.Model):
    __tablename__ = 'device_type'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)

    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    default_unit_id = db.Column(db.String(36), db.ForeignKey('unit.id'), nullable=True)

    # связи
    devices = db.relationship('Device', backref='device_type', lazy=True)


# 🔷 Device
class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)

    room_id = db.Column(db.String(36), db.ForeignKey('room.id'), nullable=False)
    device_type_id = db.Column(db.String(36), db.ForeignKey('device_type.id'), nullable=False)

    name = db.Column(db.String(255), nullable=False)
    protocol = db.Column(db.String(50), nullable=True)
    api_endpoint = db.Column(db.Text, nullable=True)

    status = db.Column(db.String(50), nullable=False, default='active')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # связи
    telemetry = db.relationship('Telemetry', backref='device', lazy=True)


# 🔷 Telemetry
class Telemetry(db.Model):
    __tablename__ = 'telemetry'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    device_id = db.Column(db.String(36), db.ForeignKey('device.id'), nullable=False)
    unit_id = db.Column(db.String(36), db.ForeignKey('unit.id'), nullable=False)

    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)
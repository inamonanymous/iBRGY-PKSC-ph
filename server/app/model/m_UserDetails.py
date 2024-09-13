from app.ext import db
from app.model import get_uuid, dt

class UserDetails(db.Model):
    __tablename__ = 'userdetails'
    id = db.Column(db.String(32), default=get_uuid, unique=True, primary_key=True)
    user_id = db.Column(db.String(32), db.ForeignKey('users.id'), nullable=False, unique=True)
    village_id = db.Column(db.String(32), db.ForeignKey('villages.id'), nullable=True)
    brgy_street_id = db.Column(db.String(32), db.ForeignKey('brgystreets.id'), nullable=True)
    house_number = db.Column(db.Integer, nullable=False)
    lot_number = db.Column(db.Integer, nullable=True)
    block_number = db.Column(db.Integer, nullable=True)
    village_street = db.Column(db.String(255), nullable=True)
    email_address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    phone_number2 = db.Column(db.String(15), nullable=True)
    selfie_photo_path = db.Column(db.String(255), nullable=True)
    gov_id_photo_path = db.Column(db.String(255), nullable=True)
    date_created = db.Column(db.DateTime, default=dt.datetime.now())
    last_modified = db.Column(db.DateTime, default=dt.datetime.now())
    modified_by = db.Column(db.String(255), nullable=False)

    users = db.relationship('Users', backref=db.backref('userdetails', lazy=True))

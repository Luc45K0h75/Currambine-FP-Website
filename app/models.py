from datetime import datetime
from app import db

# Setup doctor types for categorisation
class DoctorType(db.Model):
    __tablename__ = 'doctor_types'
    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    profiles = db.relationship('Profile', back_populates='category', lazy=True)

    def __repr__(self):
        return f'<DoctorType {self.type}>'

# Setup up profile table for each doctor/specialist
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(5), nullable=False)
    qualifications = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    doctor_type = db.Column(db.Integer, db.ForeignKey('doctor_types.type_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.relationship('DoctorType', back_populates='profiles')

    def __repr__(self):
        return f'<Profile {self.name}>'

# News posts managed via admin panel
class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published = db.Column(db.Boolean, default=True)  # False = draft, True = live

    def __repr__(self):
        return f'<News {self.title}>'
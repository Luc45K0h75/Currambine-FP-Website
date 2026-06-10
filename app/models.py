from datetime import datetime
from app import db

# Setup up profile table for each doctor/specialist
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(2), nullable=False)
    qualifications = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    doctor_type = db.Column(db.Integer, db.ForeignKey('doctor_types.type_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self):
        return f'<Profile {self.name}>'
    
# Setup doctor types for categorisation
class DoctorType(db.Model):
    __tablename__ = 'doctor_types'
    type_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<DoctorType {self.name}>'
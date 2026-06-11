from app import create_app
from app.models import Profile, DoctorType
from app import db
import json

app = create_app()

with app.app_context():
    with open('seed_data.json', 'r') as f:
        data = json.load(f)

    # Import doctor types
    for t in data['types']:
        doctor_type = DoctorType(type_id=t['type_id'], type=t['type'])
        db.session.add(doctor_type)
    db.session.commit()
    print(f"Imported {len(data['types'])} doctor types")

    # Import profiles
    for p in data['profiles']:
        profile = Profile(
            name=p['name'],
            title=p['title'],
            qualifications=p['qualifications'],
            bio=p['bio'],
            doctor_type=p['doctor_type'],
            image_url=p['image_url']
        )
        db.session.add(profile)
    db.session.commit()
    print(f"Imported {len(data['profiles'])} profiles")
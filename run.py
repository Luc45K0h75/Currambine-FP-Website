from dotenv import load_dotenv
from app import create_app, db
from app.models import Profile, DoctorType

load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
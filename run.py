from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / '.env')
from app import create_app, db
from app.models import Profile, DoctorType

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
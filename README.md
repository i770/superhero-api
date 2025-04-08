# 🦸 Superhero API

This is a RESTful API built with Flask that allows clients to interact with a fictional universe of superheroes and their powers. It demonstrates key backend development concepts such as routing, models, validations, relationships, and API design principles.

---

## 📚 Project Overview

The API allows users to:

- Retrieve a list of all heroes
- View detailed hero information, including powers
- View and update individual powers
- Assign powers to heroes with specific strength levels
- Handle proper request methods and error handling

The application is built using Flask, SQLAlchemy, and Flask-Migrate, and includes relational database logic with cascading deletes and serialization techniques.

---

## 🛠 Technologies Used

- Python 3.10+
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite (default)
- Postman (for API testing)

---

## 📁 File Structure



Create a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set the Flask App Environment Variable
bash
Copy
Edit
export FLASK_APP=manage.py
5. Run Migrations
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
6. Seed the Database
bash
Copy
Edit
python seed.py
This will add heroes and powers to the database.

7. Start the Development Server
bash
Copy
Edit
flask run
Navigate to http://127.0.0.1:5000/heroes to confirm the server is running and returning hero data.

🔌 API Endpoints
GET /heroes
Returns a list of all heroes.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  {
    "id": 2,
    "name": "Doreen Green",
    "super_name": "Squirrel Girl"
  }
]
GET /heroes/<int:id>
Returns a single hero with their associated powers.

Success Response:

json
Copy
Edit
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "strength": "Strong",
      "hero_id": 1,
      "power_id": 2,
      "power": {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly through the skies at supersonic speed"
      }
    }
  ]
}
If hero not found:

json
Copy
Edit
{
  "error": "Hero not found"
}
GET /powers
Returns a list of all powers.

Response:

json
Copy
Edit
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  },
  ...
]
GET /powers/<int:id>
Returns a specific power.

Success Response:

json
Copy
Edit
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
If power not found:

json
Copy
Edit
{
  "error": "Power not found"
}
PATCH /powers/<int:id>
Updates a power's description.

Request Body:

json
Copy
Edit
{
  "description": "This power allows a person to fly at incredible speed."
}
Success Response:

json
Copy
Edit
{
  "id": 2,
  "name": "flight",
  "description": "This power allows a person to fly at incredible speed."
}
Validation Failure:

json
Copy
Edit
{
  "errors": ["Description must be at least 20 characters long."]
}
POST /hero_powers
Creates a new HeroPower (links a hero to a power with strength).

Request Body:

json
Copy
Edit
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}
Success Response:

json
Copy
Edit
{
  "id": 11,
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average",
  "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
}
Validation Failure:

json
Copy
Edit
{
  "errors": ["Strength must be 'Strong', 'Weak', or 'Average'."]
}
✅ Validations
Power.description must be present and at least 20 characters long

HeroPower.strength must be one of: "Strong", "Weak", "Average"

🧪 Testing with Postman
Open Postman

Import the collection file: challenge-2-superheroes.postman_collection.json

Use the pre-built requests to test all endpoints

Observe response data and validation messages

📌 Tips
Always restart the server after changing model relationships or structure.

Use flask db migrate and flask db upgrade after editing models.

Seed the database whenever you reset or clear app.db.

📜 License
This project is open-source and licensed under the MIT License.

👨‍💻 Author
Isaac
Built as part of Moringa School Phase 4 Flask Code Challenge
GitHub: @yourusername

🙌 Acknowledgments
Special thanks to Moringa instructors, mentors, and fellow students for guidance, review, and support in building this project.

yaml
Copy
Edit


    Endpoint to test on postman

http://localhost:5555/powers   


 http://localhost:5555/heroes    


 http://localhost:5555/hero_powers
 
 

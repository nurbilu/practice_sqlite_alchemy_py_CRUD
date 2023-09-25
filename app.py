from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'  # SQLite database file
db = SQLAlchemy(app)

# Create a model for the table
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=True)

    def __init__(self, full_name, age, address):
        self.full_name = full_name
        self.age = age
        self.address = address

# Create the database and tables
# with app.app_context():
#     db.create_all()

# Routes for CRUD operations

# Create a new person
@app.route('/person', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = Person(**data)
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

# Read all people
@app.route('/people', methods=['GET'])
def read_people():
    people = Person.query.all()
    result = []
    for person in people:
        person_data = {
            'id': person.id,
            'full_name': person.full_name,
            'age': person.age,
            'address': person.address
        }
        result.append(person_data)
    return jsonify(result)

# Read a single person by ID
@app.route('/person/<int:id>', methods=['GET'])
def read_person(id):
    person = Person.query.get(id)
    if person:
        person_data = {
            'id': person.id,
            'full_name': person.full_name,
            'age': person.age,
            'address': person.address
        }
        return jsonify(person_data)
    else:
        return jsonify({'message': 'Person not found'}), 404

# Update a person by ID
@app.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    person = Person.query.get(id)
    if person:
        person.full_name = data.get('full_name', person.full_name)
        person.age = data.get('age', person.age)
        person.address = data.get('address', person.address)
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'})
    else:
        return jsonify({'message': 'Person not found'}), 404

# Delete a person by ID
@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})
    else:
        return jsonify({'message': 'Person not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

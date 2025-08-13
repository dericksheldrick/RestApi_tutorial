
from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


migrate = Migrate(app, db)

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Drink {self.name} - ${self.price} - {self.description}>"

@app.route('/')
def index():
    return "Hello, Welcome to the Drinks API!"

@app.route('/drinks')
def get_drinks():
    drinks = Drinks.query.all()

    list = []
    for drink in drinks:
        list.append({
            'id': drink.id,
            'name': drink.name,
            'price': drink.price,
            'description': drink.description
        })
    
    return {'drinks': list}

@app.route('/drinks/<int:drink_id>')
def get_drink(drink_id):
    drink = Drinks.query.get_or_404(drink_id)
    return {
        'id': drink.id,
        'name': drink.name,
        'price': drink.price,
        'description': drink.description
    }

@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.get_json()
    new_drink = Drinks(
        name=data['name'],
        price=data['price'],
        description=data.get('description', '')
    )
    db.session.add(new_drink)
    db.session.commit()
    return jsonify({'message': 'Drink added successfully!'}), 201

@app.route('/drinks/<int:drink_id>', methods=['PUT'])
def update_drink(drink_id):
    drink = Drinks.query.get_or_404(drink_id)
    data = request.get_json()
    
    drink.name = data['name']
    drink.price = data['price']
    drink.description = data.get('description', '')
    
    db.session.commit()
    return jsonify({'message': 'Drink updated successfully!'})

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])    
def delete_drink(drink_id):
    drink = Drinks.query.get_or_404(drink_id)
    db.session.delete(drink)
    db.session.commit()
    return jsonify({'message': 'Drink deleted successfully!'})

if __name__ == '__main__':
    db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
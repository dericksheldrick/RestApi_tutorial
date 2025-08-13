from application import app, db, Drinks

def seed_data():
    # Create the database tables
    with app.app_context():
        db.drop_all()  # Optional: drop existing tables

        db.create_all()

        # Seed the database with initial data
        drink1 = Drinks(name='Coke', price=1.50, description='A refreshing cola drink')
        drink2 = Drinks(name='Pepsi', price=1.50, description='A popular cola drink')
        drink3 = Drinks(name='Water', price=0.00, description='Pure and refreshing water')

        # Add the drinks to the session
        db.session.add(drink1)
        db.session.add(drink2)
        db.session.add(drink3)

        # Commit the session to save the changes
        db.session.commit()
        print("Database seeded with initial data.")

if __name__ == '__main__':
        seed_data()
        print("Seed data script executed successfully.")
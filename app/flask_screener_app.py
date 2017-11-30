from app import setup_app, db
from blueprints.routes import navRoutes, viewRoutes
app = setup_app()
app.register_blueprint(navRoutes.router)
app.register_blueprint(viewRoutes.router)
from app.lib.models.User import User

# setup db users for injection results
with app.app_context():
    try:
        db.drop_all()
        db.create_all()
        admin = User(username="admin", email="tif@asd.com")
        user1 = User(username='party-er', email='littyspaghetti@ooogle.com')
        user2 = User(username='super-admin', email='supersecure@security.com')
        db.session.add(admin)
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
    except Exception as e:
        result = e.message
        print(result)

 #   app.run(debug=True)


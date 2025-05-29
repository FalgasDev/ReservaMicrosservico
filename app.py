from config import app, db
from controllers.reserva_route import booking

app.register_blueprint(booking)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
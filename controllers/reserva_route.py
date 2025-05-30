from flask import Blueprint, request, jsonify
from models.reserva_model import addBooking, getBookings
from errors import ClassroomNotExist, ClassroomAlreadyReserved

booking = Blueprint("booking", __name__)

@booking.route('/')
def status():
    return 'API de Reserva de Salas funcionando! Altere para (/reservas) para visualizar'

@booking.route("/reservas", methods=["POST"])
def create_booking():
    data = request.json
    try:
        addBooking(data)
        return jsonify(data), 201
    except ClassroomNotExist as err:
        return jsonify({"Error": str(err)}), 404
    except ClassroomAlreadyReserved as err:
        return jsonify({"Error": str(err)}), 409

@booking.route("/reservas", methods=["GET"])
def get_bookings():
    return jsonify(getBookings())
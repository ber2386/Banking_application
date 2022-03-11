from customer_error.invalid_information import InvalidInformation
from dal_layer.banking.banking_dao_imp import DaoBankingImp
from customer_error.id_not_found import IdNotFound
from Service_layer.banking_service.banking_service_imp import BankingServiceImp
from flask import Flask, jsonify, request
from Service_layer.Customer.customer_service_imp import CustomerServiceImp
from dal_layer.customer.customer_dao_imp import CustomerDAOImp
from customer_error.record_not_found import RecordNotFound
from entities.bank_customers import Customer

app: Flask = Flask(__name__)
bank_dao_layer = DaoBankingImp()
bank_service_layer = BankingServiceImp(bank_dao_layer)
customer_dao_layer = CustomerDAOImp()
customer_service_layer = CustomerServiceImp(customer_dao_layer)
"""
To maintain a uniform interface, I will be using the path "/banking" for all request to my application that have to do
with banking data. I can use different verbs to determine WHAT I am doing with the team data, and that is how Flask will
know what particular service method needs to be called
"""

"""
This will allow you to create a customer from the web.
"""


@app.route("/banking", methods=["POST"])
def create_bank():
    try:
        customer_data: dict = request.get_json()
        new_customer = Customer(customer_data["customerId"], customer_data["firstName"], customer_data["lastName"])
        result = customer_service_layer.service_create_customer(new_customer)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except InvalidInformation as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


"""
This returns a customer id 
"""


@app.route("/customer/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    try:
        result: Customer = customer_service_layer.service_get_customer_id(customer_id)
        result_dictionary = result.convert_to_dictionary()
        return jsonify(result_dictionary), 200

    except RecordNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()
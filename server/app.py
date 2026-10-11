
from flask import Flask, Response, jsonify

app = Flask(__name__)

# Sample contract records
contracts = [
    {
        "id": 1,
        "title": "Software Development Agreement",
        "customer": "Alice",
        "contractor": "John",
        "value": 50000
    },
    {
        "id": 2,
        "title": "Website Maintenance Agreement",
        "customer": "Brian",
        "contractor": "Mary",
        "value": 30000
    }
]

# Sample customer records
customers = [
    {"name": "Alice"},
    {"name": "Brian"}
]


@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):
    # Search for a contract with the requested ID
    for contract in contracts:
        if contract["id"] == id:
            return jsonify(contract), 200

    # No contract with that ID was found
    return jsonify({"error": "Contract not found"}), 404


@app.route("/customer/<string:customer_name>", methods=["GET"])
def get_customer(customer_name):
    # Check whether the customer exists
    for customer in customers:
        if customer["name"].lower() == customer_name.lower():
            # Confirm existence without exposing customer information
            return Response(status=204)

    # Customer does not exist
    return jsonify({"error": "Customer not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

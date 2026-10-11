
from flask import Flask, Response

app = Flask(__name__)

# Sample contract records
contracts = [
    {
        "id": 1,
        "contract_information": "This contract is for John and building a shed"
    },
    {
        "id": 2,
        "contract_information": "This contract is for a deck for a buisiness"
    },
    {
        "id": 3,
        "contract_information": "This contract is to confirm ownership of this car"
    }
]

# Sample customer records
customers = ["bob", "bill", "john", "sarah"]


@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):
    # Search for a contract with the requested ID
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200

    # No contract with that ID was found
    return "Contract not found", 404


@app.route("/customer/<string:customer_name>", methods=["GET"])
def get_customer(customer_name):
    # Check whether the customer exists
    if customer_name.lower() in customers:
        # Confirm existence without exposing customer information
        return Response(status=204)

    # Customer does not exist
    return "Customer not found", 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)

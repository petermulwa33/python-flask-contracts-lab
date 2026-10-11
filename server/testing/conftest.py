
#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

# Contract information
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

# Customer names
customers = ["bob", "bill", "john", "sarah"]


# GET route: retrieve contract information
@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200

    return "Contract not found", 404


# GET route: check whether a customer exists
@app.route("/customer/<string:customer_name>", methods=["GET"])
def get_customer(customer_name):
    if customer_name.lower() in customers:
        # Do not expose sensitive customer information
        return Response(status=204)

    return "Customer not found", 404


if __name__ == "__main__":
    app.run(port=5555, debug=True)


from flask import Flask, jsonify, request
import stripe
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

stripe.api_key = "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"

@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    try:
        data = request.get_json()
        amount = data.get("amount", 18900)
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="eur",
            automatic_payment_methods={"enabled": True}
        )
        return jsonify({"clientSecret": intent.client_secret})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

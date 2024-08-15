from flask import Flask, request, jsonify
from sendEmail import send_email_via_postman

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.json
    result = send_email_via_postman(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)



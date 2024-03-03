from flask import Flask, request, jsonify

app = Flask(__name__)

user_data = [
    {
        "user_id": "123",
        "name": "Anand",
        "email": "anandharikrishnan14@gmail.com"
    }
]

@app.route("/get-user")
def get_user():
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    user_data.append(data)
    return jsonify(user_data), 201

if __name__ == "__main__":
    app.run(debug=True)

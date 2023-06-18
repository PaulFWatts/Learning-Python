from flask import Flask, app, request, jsonify

app = Flask(__name__)   # Flask app

@app.route("/get-user/<user_id>")    # at the end point /get-user/<user_id>
def get_user(user_id):            # call method get_user
    user_data =  {         # create python dictionary (mock data)
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")   # get extra query parameter
    if extra:                           # if extra is present
        user_data["extra"] = extra      # add extra to user_data
        
    return jsonify(user_data), 200           # return user_data as JSON

@app.route("/create-user", methods=["POST"])    # at the end point /create-user
def create_user():                              # call method create_user
    data = request.get_json()                   # get JSON data from request
    
    return jsonify(data), 201                   # return data as JSON

if __name__ == "__main__":          # on running python main.py
    app.run(debug=True)             # run the flask app
    
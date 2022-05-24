from flask import Flask, request

app= Flask('__main__')

users={
    "first_name" : "Omar",
    "last_name" : "Ramos",
    "yy-mm-dd" : "02-05-21",
}

@app.route('/', methods=['GET'])
def go_home():
    return 'Hello World'

@app.route('/users', methods=['POST'])
def set_user():
    user= request.json
    print(user)
    return user

@app.route('/users', methods=['GET'])
def get_users():
    return users

@app.route('/devices', methods=['POST'])
def set_device():
    device= request.json
    print(device)
    return device, 201

@app.route('/inclination', methods=['POST'])
def set_inclinacion():
    device= request.json
    print(device)
    return device, 201
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
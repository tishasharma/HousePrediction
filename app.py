from flask import Flask, request, jsonify
import pickle
import numpy as np
import json

app = Flask(__name__)

# Load the saved model
model = pickle.load(open('bangalore_home_price_model.pkl', 'rb'))

# Load feature columns from JSON
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

def predict_price(location, sqft, bath, bhk, data_columns, lr_clf):
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location in data_columns:
        loc_index = data_columns.index(location.lower())
        x[loc_index] = 1
    return lr_clf.predict([x])[0]

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.json
    location = data['location']
    total_sqft = data['total_sqft']
    bath = data['bath']
    bhk = data['bhk']
    
    # Predict the price
    prediction = predict_price(location, total_sqft, bath, bhk, data_columns, model)
    
    return jsonify({'predicted_price': prediction})

if __name__ == "__main__":
    app.run(debug=True)

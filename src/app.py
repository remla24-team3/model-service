import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import keras
import pickle

from gdown import download_folder
from flask import Flask, request
from tensorflow.keras.preprocessing.sequence import pad_sequences

SEQUENCE_LENGTH = 200

model = None
app = Flask(__name__)

@app.route('/API/v1.0/predict', methods=['GET', 'POST'])
def predict():
    url = request.args["url"]
    prediction = model.predict([preprocess(url)])
    
    encoder = pickle.load(open('model/encoder.pickle', 'rb'))
    
    prediction = encoder.inverse_transform([prediction.argmax(axis=1)[0]])[0]
    
    return str(prediction)

# TODO: Move to lib-ml
def preprocess(input):
    tokenizer = pickle.load(open('model/tokenizer.pickle', 'rb'))
    result = pad_sequences(tokenizer.texts_to_sequences(input), maxlen=SEQUENCE_LENGTH)
    return result


if __name__ == '__main__':
    
    # download the model
    # DRIVE_ID = '1IufuHUEvaFgWJzmHJEogi4NEUIeV1BpJ'
    # download_folder(id=DRIVE_ID, output="artifacts", quiet=False)
    
    # load the model
    model: keras.Sequential = keras.models.load_model('model/model.keras')
    app.run(host='0.0.0.0', port=105, debug=True)
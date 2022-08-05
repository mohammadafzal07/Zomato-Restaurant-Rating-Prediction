import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pymongo
import logging

logging.basicConfig(filename='info.txt', 
                    level=logging.INFO,
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M-%S')

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():

    logging.info("Accessing index.html!!!")
    return render_template('index.html')


@app.route('/prdict',methods=['POST'])
def predict():

    '''
    For rendering results on HTML GUI
    '''

    if request.method == 'POST':
            a = request.form["Online Order"]
            b = request.form["Book Table"]
            c = request.form["Votes"]
            d = request.form["Restaurant Type"]
            e = request.form["Cuisines"]
            f = request.form["Cost"]
            g = request.form["Type"]
            h = request.form["Location"]

            logging.info("Successfully retrieved information from user")
            
    default_connection_url = "mongodb+srv://afzal:afzal123@cluster0.uzpfsbd.mongodb.net/test"
    client = pymongo.MongoClient(default_connection_url)
    logging.info('Successfully retrieved info from user')

    db_name = "Zomato"
    database = client[db_name]
    print("DB Created")
    collection_name = 'user_details'
    collection = database[collection_name]
    print('collection Created')



    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1)

    info = {
                'Online Order':a,
                'Book Table': b,
                'Votes': c,
                'Restaurant Type': d,
                'Cuisines': e,
                'Cost': f,
                'Type': g,
                'Location': h,
		'Rating Prediction' : output,
            }
        
    collection.insert_one(info)
    logging.info('Data inserted')

    logging.info("successfully predicted")
    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)

    #app.run(debug=True)

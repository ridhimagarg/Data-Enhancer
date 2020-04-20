## Importing libraries, utility function
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import pandas as pd
import requests, json, os
# from data_enhancer_v2.main import main
from main import main
from utils.basic_utils import *

##------------------------------------ Initializing application -------------------------##

## Creating a flask app
app = Flask(__name__,)
app.secret_key = 'some_secret'
Bootstrap(app)

## variable for storing the website url to scrape
website = ''
UPLOAD_FOLDER = '../data/raw/'
ALLOWED_EXTENSIONS = {'json'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

##---------------------------------- Function connecting templates(html file:bootstrap) -------------------------##
##---------------------------------- Index page(home page)-----------------##
@app.route('/', methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':

        print("Entered into post..")

        if 'file' not in request.files:
            print("1..")
            flash('No file part')
            return redirect(request.url)
        print("file chosen")

        file = request.files['file']
        if file.filename == '':
            print("2..")
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("3...")
            filename = secure_filename(file.filename)
            list_file_num = [int(file.split('_')[1].split('.')[0]) for file in os.listdir(UPLOAD_FOLDER) if file.endswith('.json')]
            print(str(max(list_file_num)))
            print(str(max(list_file_num)+1))
            filename = 'sample_'+str(max(list_file_num)+1)+'.json'
            # for file in os.listdir(UPLOAD_FOLDER):
            #     if file.endswith('.json'):
            #         file.split('_')[1].split('.')[0]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            get_text = read_json(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            get_text = get_text["text"]
            print(os.getcwd())
            os.chdir("../")
            print(os.getcwd())
            final_predictions = main(filename)
            print(final_predictions)
            flash('File Uploaded Successfully!!')
            os.chdir(os.path.join(os.getcwd(), "flask-app"))
            return render_template('predict.html', text=get_text, prediction = final_predictions)
            # return redirect(url_for('.index',))
    else:

        # os.chdir(os.path.join(os.getcwd(), "flask-app"))

        return render_template('index.html')

##-------------------------- Get input(business name) from form at index.html page and fetching data from api--------------------##
## Fetching data from google API

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        print("atleast")
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Incorrect file extenstion. Must be .TXT!', 'danger')
            return redirect(url_for('/',
                                    ))
        # file.save(f.filename)
        return 'file uploaded successfully'


@app.route('/predict', methods=['POST'])
def predict():

    global website

    if request.method == 'POST':

        search = request.form['search']

        ## Calling function get_details from utilities_google_api, for getting information of business
        business_information, website = uga.get_details(search)

        ## Passed this information to results.html file
        return render_template('results.html', len= len(business_information), prediction = business_information)


##-----------------------------------------------Website crawl ---------------------------------------------##

## Crawling the website after fetching the website url from that API
@app.route('/crawled_information', methods=['POST'])                        
def crawled_information():

    global website

    ## Getting information through crawler, utilities_crwaler.py file contains crawler code.
    emails, phone_numbers, addresses = uc.get_information(website)

    ## We Have to make list as flask iterate over list only.
    emails = list(set(emails))
    phone_numbers = list(set(phone_numbers))
    addresses = list(set(addresses))

    ## returning data to resuts_new.html file.
    return render_template('results_new.html',website = website, len_email = len(emails), len_phone = len(phone_numbers), len_address = len(addresses), email = emails, phone_number = phone_numbers, address = addresses)                

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug= True)

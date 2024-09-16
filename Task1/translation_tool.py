from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests
import os


app = Flask(__name__) #Initialize the Flask Application
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY') # Load the API Key from Environment Variables 
#Advantages of using .env file: It enhances security by keeping sensitive information (like API keys) separate from your code, protects your credentials from being exposed in version control by adding .env to .gitignore, allows easy management of different configurations for multiple environments (development, production, etc.), and simplifies collaboration by letting each team member maintain their own .env files without altering shared code.

@app.route('/') #Define the Home Route
def home():
    return render_template('translate.html')  # This will serve your index.html file


@app.route('/translate', methods=['GET', 'POST'])
def translate(): #Inside this function, you’ll process the incoming request, extract data (like the text to be translated), and call the Google Translate API to return the translation.
    if request.method == 'POST':
        data = request.json
        text = data['text']
        target_language = data['target']
        source_language = data['source']

        # Google Translate API URL
        url = f"https://translation.googleapis.com/language/translate/v2"
        #When your Flask app needs to translate text, it communicates with the Google Translate service over the internet. The API endpoint (URL) specifies exactly where your request is being sent to get the service from Google.
        #In this case, the URL https://translation.googleapis.com/language/translate/v2 is where Google hosts their Translate API. Without this URL, your app wouldn't know where to send the request for translation.
        
        #This block creates a dictionary of parameters that will be sent to the Google Translate API as query parameters.
        params = {
            'q': text,
            'target': target_language,
            'source': source_language,
            'key': GOOGLE_API_KEY
        }
        
        response = requests.post(url, params=params)
        #This line sends a POST request to the Google Translate API endpoint using the requests library.
        #It passes the url and the params (the text, target language, source language, and API key) to the API.
        #The API processes this request and returns a response, which is stored in the response variable.
        
        result = response.json()
        #This converts the response from the API (which is in JSON format) into a Python dictionary so that it can be easily worked with in the code.

        translated_text = result['data']['translations'][0]['translatedText']
        
        return jsonify({"translatedText": translated_text})
    
    else:
        return 'Use POST request to submit data for translation.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)

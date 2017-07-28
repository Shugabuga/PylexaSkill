import json
import os
import requests

from flask import Flask

from pylexa.app import alexa_blueprint
from pylexa.intent import handle_intent
from pylexa.app import handle_launch_request
from pylexa.response import PlainTextSpeech


app = Flask(__name__)
app.config['app_id'] = os.getenv('ALEXA_APP_ID')
app.register_blueprint(alexa_blueprint)

@handle_intent('GetBTC')
def handle_info_intent(request):
    try:
        print('Debug: ' + str(request.slots))
        # get rounded BTC value
        btcValue = exec(os.environ['ENDPOINT'])
        print(btcValue)
        # /get rounded BTC value
        return PlainTextSpeech(os.environ['BEFORE'] + " " + btcValue + " " + os.environ['AFTER'])
    except:
        return PlainTextSpeech("I don't know.")


@handle_intent('A')
@handle_launch_request
def handle_start_message(request):
    try:
        print("New launch!")
        # get rounded BTC value
        btcValue = exec(os.environ['ENDPOINT'])
        print(btcValue)
        # /get rounded BTC value
        return PlainTextSpeech(os.environ['BEFORE'] + " " + btcValue + " " + os.environ['AFTER'])
    except:
        return PlainTextSpeech("I don't know.")

if __name__ == '__main__':
    app.run(debug=True)

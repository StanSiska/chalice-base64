from chalice import Chalice
from chalice import BadRequestError
from chalice import ChaliceViewError

import base64
import sys

app = Chalice(app_name='chalice-hashing-microservice')

# Enable debugging for developmemt
app.debug = True

@app.route('/')
def display_welcome():
    """Displays welcome message"""
    return {'Welcome': 'Base64 Enc/Dec Microservice'}

@app.route('/encode/{string}')
def encode_string(string):
    """Encode string by Base64"""
    try:
        resp = base64.b64encode(string)
        return {'response': resp}
    except TypeError:
        raise BadRequestError("Invalid string, check your input.")

@app.route('/decode/{string}')
def decode_string(string):
    """Decode Base64 string"""
    try:
        resp = base64.b64decode(string)
        return {'response': resp}
    except UnicodeDecodeError as exc:
        raise ChaliceViewError("Invalid start byte" + str(exc))
    except TypeError:
        raise ChaliceViewError("Error during decoding, possibly not an Base64 input.")
    except:
        print "Unexpected error:", sys.exc_info()[0]
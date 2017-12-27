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

@app.route('/b64e/{string_to_enc}')
def encode_string(string_to_enc):
    """Encode string by Base64"""
    try:
        resp = base64.b64encode(string_to_enc)
        return {'response': resp}
    except TypeError:
        raise BadRequestError("Invalid string, check your input.")

@app.route('/b64d/{string_to_dec}')
def decode_string(string_to_dec):
    """Decode Base64 string"""
    try:
        resp = base64.b64decode(string_to_dec)
        return {'response': resp}
    except UnicodeDecodeError as exc:
        raise ChaliceViewError("Invalid start byte" + str(exc))
    except TypeError:
        raise ChaliceViewError("Error during decoding, possibly not an Base64 input.")
    except:
        print "Unexpected error:", sys.exc_info()[0]
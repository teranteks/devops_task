from flask import Flask, json
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

@app.route("/healthcheck")
def health_check():
    """
    Return HTTP 200 OK Status
    """
    return json.dumps("HTTP 200 OK"), 200, {'ContentType':'application/json'} 

@app.route('/<regex("((www)?[\w./-:]+[^(healthcheck)]+[\w:./-_]+)|^\/"):not_found>')
def bad_request(not_found):
    """
    Return HTTP 404. Incase of matching regex
    """
    return json.dumps(f"HTTP 404 Not Found URL: {not_found} "), 404, {'ContentType':'application/json'}

@app.route('/')
def empty():
    """
    Return HTTP 404. Incase of matching regex
    """
    return json.dumps("HTTP 404 Not Found"), 404, {'ContentType':'application/json'}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, abort
from meetings import get_meetings
from metrics import get_metrics
from credentials import validate_token

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/meetings/<string:meeting_id>/<string:meetings_type>', methods=['GET'])
def meeting_registrants(meeting_id, meetings_type):
    if not request.headers['Authorization']:
        abort(401)
    else:
        if validate_token(request.headers['Authorization']):
            return get_meetings(meetings_type, meeting_id)
        else:
            abort(403)


@app.route("/metrics/<string:metrics_type>/<string:meeting_id>/<string:metrics_subtype>", methods=['GET'])
def metrics(metrics_type, meeting_id, metrics_subtype):
    if not request.headers['Authorization']:
        abort(401)
    else:
        if validate_token(request.headers['Authorization']):
            return get_metrics(metrics_type, metrics_subtype, meeting_id)
        else:
            abort(403)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8080)

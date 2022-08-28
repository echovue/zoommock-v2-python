from flask import Flask, jsonify, request, send_file, abort
from meetings import get_meetings
from metrics import get_metrics
from credentials import token

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/meetings/<string:meeting_id>/<string:meetings_type>', methods=['GET'])
def meeting_registrants(meeting_id, meetings_type):
    if request.headers['Authorization'] != 'Bearer ' + token:
        abort(403)
    return get_meetings(meetings_type, meeting_id)


@app.route("/metrics/<string:metrics_type>/<string:meeting_id>/<string:metrics_subtype>", methods=['GET'])
def metrics(metrics_type, meeting_id, metrics_subtype):
    if request.headers['Authorization'] != 'Bearer ' + token:
        abort(403)
    return get_metrics(metrics_type, metrics_subtype, meeting_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8080)

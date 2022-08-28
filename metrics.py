from flask import Flask, jsonify, request, send_file, abort
from credentials import token


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/meetings/123456/registrants', methods=['GET'])
def registrants():
    if request.headers['Authorization'] != 'Bearer ' + token:
        abort(403)
    print(request.headers['Authorization'])
    return """{
                  "next_page_token": "w7587w4eiyfsudgf",
                  "page_count": 1,
                  "page_size": 30,
                  "total_records": 20,
                  "registrants": [
                    {
                      "id": "9tboDiHUQAeOnbmudzWa5g",
                      "address": "1800 Amphibious Blvd.",
                      "city": "Mountain View",
                      "comments": "Looking forward to the discussion.",
                      "country": "US",
                      "custom_questions": [
                        {
                          "title": "What do you hope to learn from this?",
                          "value": "Look forward to learning how you come up with new recipes and what other services you offer."
                        }
                      ],
                      "email": "jchill@example.com",
                      "first_name": "Jill",
                      "industry": "Food",
                      "job_title": "Chef",
                      "last_name": "Chill",
                      "no_of_employees": "1-20",
                      "org": "Cooking Org",
                      "phone": "5550100",
                      "purchasing_time_frame": "1-3 months",
                      "role_in_purchase_process": "Influencer",
                      "state": "CA",
                      "status": "approved",
                      "zip": "94045",
                      "create_time": "2022-03-22T05:59:09Z",
                      "join_url": "https://example.com/j/11111"
                    }, 
                    {
                      "id": "77tbDiHUQAeOnbmudzWa5g",
                      "address": "1800 Amphibious Blvd.",
                      "city": "Mountain View",
                      "comments": "Looking forward to the discussion.",
                      "country": "US",
                      "custom_questions": [
                        {
                          "title": "What do you hope to learn from this?",
                          "value": "Look forward to learning how you come up with new recipes and what other services you offer."
                        }
                      ],
                      "email": "asmith@example.com",
                      "first_name": "Adam",
                      "industry": "Food",
                      "job_title": "Chef",
                      "last_name": "Smith",
                      "no_of_employees": "1-20",
                      "org": "Cooking Org",
                      "phone": "5550100",
                      "purchasing_time_frame": "1-3 months",
                      "role_in_purchase_process": "Influencer",
                      "state": "CA",
                      "status": "approved",
                      "zip": "94045",
                      "create_time": "2022-03-22T05:59:09Z",
                      "join_url": "https://example.com/j/11111"
                    },
                    {
                      "id": "77tboDiHUQAeOnbmudzWa5g",
                      "address": "1800 Amphibious Blvd.",
                      "city": "Mountain View",
                      "comments": "Looking forward to the discussion.",
                      "country": "US",
                      "custom_questions": [
                        {
                          "title": "What do you hope to learn from this?",
                          "value": "Look forward to learning how you come up with new recipes and what other services you offer."
                        }
                      ],
                      "email": "aroman@example.com",
                      "first_name": "Alex",
                      "industry": "Food",
                      "job_title": "Chef",
                      "last_name": "Roman",
                      "no_of_employees": "1-20",
                      "org": "Cooking Org",
                      "phone": "5550100",
                      "purchasing_time_frame": "1-3 months",
                      "role_in_purchase_process": "Influencer",
                      "state": "CA",
                      "status": "approved",
                      "zip": "94045",
                      "create_time": "2022-03-22T05:59:09Z",
                      "join_url": "https://example.com/j/11111"
                    }
                    
                  ]
                }"""


@app.route('/metrics/meetings/123456/participants', methods=['GET'])
def participants():
    if request.headers['Authorization'] != 'Bearer ' + token:
        abort(403)
    print(request.headers['Authorization'])
    return """{
                  "next_page_token": "Tva2CuIdTgsv8wAnhyAdU3m06Y2HuLQtlh3",
                  "page_count": 1,
                  "page_size": 30,
                  "total_records": 1,
                  "participants": [
                    {
                      "audio_quality": "good",
                      "camera": "FaceTime HD Camera",
                      "connection_type": "UDP",
                      "customer_key": "349589LkJyeW",
                      "data_center": "United States (SC Top)",
                      "device": "Phone",
                      "domain": "example.com",
                      "email": "user@example.com",
                      "from_sip_uri": "example.com",
                      "full_data_center": "United States (SC Top);",
                      "harddisk_id": "Disk01",
                      "id": "zJKyaiAyTNC-MWjiWC18KQ",
                      "in_room_participants": 2,
                      "ip_address": "10.100.111.8",
                      "join_time": "2022-03-01T10:15:14Z",
                      "leave_reason": "Host ended the meeting.",
                      "leave_time": "2022-03-01T10:17:35Z",
                      "location": "United States",
                      "mac_addr": "f85e-a012-92d8",
                      "microphone": "Microphone (2- High Definition Audio Device)",
                      "network_type": "Wired",
                      "participant_user_id": "DYHrdpjrS3uaOf7dPkkg8w",
                      "pc_name": "HW0010449",
                      "recording": false,
                      "registrant_id": "fdgsfh2ey82fuh",
                      "role": "host",
                      "screen_share_quality": "good",
                      "share_application": true,
                      "share_desktop": true,
                      "share_whiteboard": true,
                      "sip_uri": "example.com",
                      "speaker": "speaker (2- High Definition Audio Device)",
                      "status": "in_meeting",
                      "user_id": "20162560",
                      "user_name": "jchill",
                      "version": "5.9.1.2581",
                      "video_quality": "good",
                      "bo_mtg_id": "Dkgwu8nm/ExG1vM+GhLRhA=="
                    }
                  ]
                }"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=8080)

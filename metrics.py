from meetings import get_test_users

num_participants = 6


def get_metrics(metrics_type, metrics_subtype, meeting_id):
    if metrics_type == 'meetings':
        if metrics_subtype == 'participants':
            return get_participants(meeting_id)


def get_participants(meeting_id):
    users = get_test_users()
    participants = []
    for i in range(num_participants):
        participants.append(build_participant(meeting_id, users[i], 'in meeting'))

    response = {}
    response['next_page_token'] = 'Tva2CuIdTgsv8wAnhyAdU3m06Y2HuLQtlh3'
    response['page_count'] = 1
    response['page_size'] = 30
    response['total_records'] = num_participants
    response['participants'] = participants

    return response


def build_participant(meeting_id, user, status):
    participant = {}
    participant['audio_quality'] = 'good'
    participant['camera'] = 'FaceTime HD Camera'
    participant['connection_type'] = 'UDP'
    participant['customer_key'] = '349589LkJyeW'
    participant['data_center'] = 'United States (SC Top)'
    participant['device'] = 'Phone'
    participant['domain'] = 'example.com'
    participant['email'] = user['first_name'] + '.' + user['last_name'] + '@email.com'
    participant['from_sip_uri'] = 'example.com'
    participant['full_data_center'] = 'United States (SC Top);'
    participant['harddisk_id'] = 'Disk01'
    participant['id'] = user['id']
    participant['in_room_participants'] = num_participants
    participant['ip_address'] = '10.100.111.8'
    participant['join_time'] = '2022-03-01T10:15:14Z'
    participant['leave_reason'] = 'Host ended the meeting.'
    participant['leave_time'] = '2022-03-01T10:17:35Z'
    participant['location'] = 'United States'
    participant['mac_addr'] = 'f85e-a012-92d8'
    participant['microphone'] = 'Microphone (2- High Definition Audio Device)'
    participant['network_type'] = 'Wired'
    participant['participant_user_id'] = 'user' + user['id']
    participant['pc_name'] = 'HW0010449'
    participant['recording'] = False
    participant['registrant_id'] = 'reg' + user['id']
    participant['role'] = 'host'
    participant['screen_share_quality'] = 'good'
    participant['share_application'] = True
    participant['share_desktop'] = True
    participant['share_whiteboard'] = True
    participant['sip_uri'] = 'example.com'
    participant['speaker'] = 'speaker (2- High Definition Audio Device)'
    participant['status'] = status
    participant['user_id'] = '20162560'
    participant['user_name'] = user['first_name'] + '.' + user['last_name']
    participant['version'] = '5.9.1.2581'
    participant['video_quality'] = 'good'
    participant['bo_mtg_id'] = meeting_id
    return participant

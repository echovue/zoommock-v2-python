num_registrants = 8

def get_test_users():
    users = {}
    users[0] = {'id': '9887382', 'first_name': 'Gayle', 'last_name': 'Simpson'}
    users[1] = {'id': '8552356', 'first_name': 'Aveline', 'last_name': 'Stidolph'}
    users[2] = {'id': '6254566', 'first_name': 'Arlene', 'last_name': 'Leighton'}
    users[3] = {'id': '5843245', 'first_name': 'Liliana', 'last_name': 'Moon'}
    users[4] = {'id': '2651256', 'first_name': 'Philomena', 'last_name': 'Russel'}
    users[5] = {'id': '9462156', 'first_name': 'Perlie', 'last_name': 'Aston'}
    users[6] = {'id': '3521565', 'first_name': 'Reverie', 'last_name': 'Troy'}
    users[7] = {'id': '1325685', 'first_name': 'Everitt', 'last_name': 'Mann'}
    users[8] = {'id': '8846215', 'first_name': 'Cal', 'last_name': 'Rollins'}
    users[9] = {'id': '5568652', 'first_name': 'Phillida', 'last_name': 'Oakley'}
    return users


def get_meetings(meetings_type, meeting_id):
    if meetings_type == 'registrants':
        return get_registrants(meeting_id)


def get_registrants(meeting_id):
    users = get_test_users()
    registrants = []
    for i in range(num_registrants):
        registrants.append(build_registrant(meeting_id, users[i]))

    response = {}
    response['next_page_token'] = 'Tva2CuIdTgsv8wAnhyAdU3m06Y2HuLQtlh3'
    response['page_count'] = 1
    response['page_size'] = 30
    response['total_records'] = num_registrants
    response['registrants'] = registrants

    return response


def build_registrant(meeting_id, user):
    registrant = {}
    custom_questions = {}
    custom_questions['title'] = 'What do you hope to learn from this?'
    custom_questions['value'] = 'Look forward to learning how you come up with new recipes and what other services you offer.'
    
    registrant['id'] = user['id']
    registrant['address'] = '1800 Amphibious Blvd.'
    registrant['city'] = 'Mountain View'
    registrant['comments'] = 'Looking forward to the discussion.'
    registrant['country'] = 'US'
    registrant['custom_questions'] = custom_questions
    registrant['email'] = user['first_name'] + '.' + user['last_name'] + '@email.com'
    registrant['first_name'] = user['first_name']
    registrant['industry'] = 'Food'
    registrant['job_title'] = 'Chef'
    registrant['last_name'] = user['last_name']
    registrant['no_of_employees'] = '1-20'
    registrant['org'] = 'Cooking Org'
    registrant['phone'] = '5550100'
    registrant['purchasing_time_frame'] = '1-3 months'
    registrant['role_in_purchase_process'] = 'Influencer'
    registrant['state'] = 'CA'
    registrant['status'] = 'approved'
    registrant['zip'] = '94045'
    registrant['create_time'] = '2022-03-22T05:59:09Z'
    registrant['join_url'] = 'https://example.com/j/' + meeting_id
    return registrant


num_registrants = 3


def get_meetings(meetings_type, meeting_id):
    if meetings_type == 'registrants':
        return get_registrants(meeting_id)


def get_registrants(meeting_id):
    
    registrants = []
    for i in range(num_registrants):
        userid = str(i) + '12345'
        registrants.append(build_registrant(meeting_id, userid))

    response = {}
    response['next_page_token'] = 'Tva2CuIdTgsv8wAnhyAdU3m06Y2HuLQtlh3'
    response['page_count'] = 1
    response['page_size'] = 30
    response['total_records'] = num_registrants
    response['registrants'] = registrants

    return response


def build_registrant(meeting_id, userid):
    registrant = {}
    custom_questions = {}
    custom_questions['title'] = 'What do you hope to learn from this?'
    custom_questions['value'] = 'Look forward to learning how you come up with new recipes and what other services you offer.'
    
    registrant['id'] = userid
    registrant['address'] = '1800 Amphibious Blvd.'
    registrant['city'] = 'Mountain View'
    registrant['comments'] = 'Looking forward to the discussion.'
    registrant['country'] = 'US'
    registrant['custom_questions'] = custom_questions
    registrant['email'] = 'user' + userid + '@example.com'
    registrant['first_name'] = 'first' + userid
    registrant['industry'] = 'Food'
    registrant['job_title'] = 'Chef'
    registrant['last_name'] = 'last' + userid
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

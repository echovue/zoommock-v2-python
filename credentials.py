import jwt

TEST_KEY = '1234567890'
TEST_SECRET = 'abcdefghijklmnopqrstuvwxyz'


def validate_token(header):
    try:
        result = jwt.decode(jwt=header[7:],
                            key=TEST_SECRET,
                            algorithms='HS256')
        if result and result['iss'] == TEST_KEY:
            return True
    except Exception as e:
        return False

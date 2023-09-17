import json
import os

from dotenv import load_dotenv
from requests import get, post

# id : pkwhale / pw : pkwhale1234



    
class HTTPService(object):
    def __init__(self, *args):
        super(HTTPService, self).__init__(*args)
        load_dotenv('config/.env',verbose=True)
        self.url = os.getenv('AUTH_URL')
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.body = {
        'service': os.getenv('SERVICE'),
        'userType': os.getenv('USER_TYPE'),
        'username': os.getenv('USER_NAME'),
        'password': os.getenv('PASSWORD')
        }

    def getToken(self):
        token = post(self.url, headers=self.headers, data=json.dumps(self.body)).text
        if token == None or token == '':
            raise Exception('토큰을 받아오는데 실패했습니다.')
        print('토큰 발급 성공!')
        return token
        
    
        
        
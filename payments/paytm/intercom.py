import requests
import json
from datetime import datetime

DEFAULT_DATA = {
              "email": "test@gmail.com",
              "phone": "2222222222",
              "name": "API test User2",
              "created_at": datetime.now().__str__()
            }


class IntercomLead(object):

    def __init__(self):
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': 'Bearer dG9rOjk0NDZmNzBkXzZiMzhfNDMyN19hZjE1XzBkNzgzMzEyNGE1OToxOjA='}
        self.add_api = 'https://api.intercom.io/contacts'
        self.defualt_data = {
              "email": "test@gmail.com",
              "phone": "111111111111",
              "name": "API test User"
            }

    def send_lead(self, request_data):
        response = requests.post(url=self.add_api, data=json.dumps(request_data), headers=self.headers)
        return response.content

if __name__ == "__main__":
    intercom = IntercomLead()
    response = intercom.send_lead(DEFAULT_DATA)
    print response
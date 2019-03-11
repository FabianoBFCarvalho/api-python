import json
from controller.base_request import BaseRequest
from models.contact import Contact
from google.appengine.api import search


class ContactPhoto(BaseRequest):

    def post(self):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(self.request.POST.get('profile_image'))
        print('entrou if')
        Contact.prepare_photo(self.request.POST.get('profile_image'))

        self.response_write({'db_id': ''})

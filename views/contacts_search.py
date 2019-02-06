import json

from controller.base_request import BaseRequest
from models.contact import Contact
from google.appengine.api import search


class ContactsSearch(BaseRequest):

    def get(self):
        contacts = []
        querystring = self.prepare_query_profile()
        print(querystring)

        index = search.Index(name='contacts', namespace='ac-abc123')
        search_query = search.Query(
            query_string=querystring,
            options=search.QueryOptions(
                limit=10))
        try:
            search_results = index.search(search_query)
            for doc in search_results:
                contact = Contact.convert_index_search_in_contact(doc.fields)
                contact['db_id'] = doc.doc_id
                contacts.append(contact)
            response = {
                "contacts": contacts,
                "count": search_results.number_found
            }
            self.response_write(response)
        except search.Error:
            print(search.Error)



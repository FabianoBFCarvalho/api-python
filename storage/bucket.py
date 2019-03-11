
import os
import cloudstorage
from google.appengine.api import app_identity
import webapp2
import googleapiclient.http
import base64

storage = googleapiclient.discovery.build('storage', 'v1')


class Bucket(webapp2.RequestHandler):

    def get(self):
        bucket_name = os.environ.get(
            'BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
        print('--------------------------------------------------------------')
        print(bucket_name)
        print('--------------------------------------------------------------')
        return bucket_name

    def create_file(self, file):
        """
        save file in storage
        :param file:
        :return: path_url

        """
        # new_file = base64.b64decode(file[22:])
        # new_file = base64.rpartition(',')[2]

        print("*******************************************************")
        print(file)

        # print(new_file)

        path_url = '/' + self.get() + '/image'

        storage_file = cloudstorage.open(path_url, 'w', content_type='image/jpeg')
        storage_file.write(file)
        storage_file.close()

        print('@@@@@@@@@@@@@@@@@@@  FINISH @@@@@@@@@@@@@@@@@@@@')

        return path_url


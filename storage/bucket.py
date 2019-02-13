
import os
import cloudstorage
from google.appengine.api import app_identity
import webapp2
import googleapiclient.discovery
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
        # """Create a file."""
        new_file = base64.b64decode(file[22:])
        print(file[22:])
        print(new_file)

        filename = '/' + self.get() + '/image.png'
        self.tmp_filenames_to_clean_up = []
        # self.response.write('Creating file {}\n'.format(filename))

        # The retry_params specified in the open call will override the default
        # retry params for this particular file handle.
        write_retry_params = cloudstorage.RetryParams(backoff_factor=2)
        with cloudstorage.open(
                filename, 'w', content_type='image/png',
                retry_params=write_retry_params) as cloudstorage_file:
                    cloudstorage_file.write(new_file)
                    cloudstorage_file.close()
        self.tmp_filenames_to_clean_up.append(filename)
        # return ''


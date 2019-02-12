# from beaker.ext import google
from google.cloud import storage
# import os
# import cloudstorage
# from google.appengine.api import app_identity


class Bucket:

    @staticmethod
    def create_bucket(bucket_name):
        """Creates a new bucket."""
        storage_client = storage.Client()
        bucket = storage_client.create_bucket('my-new-bucket')
        print('Bucket {} created'.format(bucket.name))

    @classmethod
    def get_bucket(cls, bucket_name):
        storage_client = storage.Client()
        try:
            bucket = storage_client.get_bucket(bucket_name)
        except():
            print("Sorry, that bucket does not exist! creating...")
            cls.create_bucket(bucket_name)

    # def get(self):
    #     bucket_name = os.environ.get(
    #         'BUCKET_NAME', app_identity.get_default_gcs_bucket_name())
    #
    #     self.response.headers['Content-Type'] = 'text/plain'
    #     self.response.write(
    #         'Demo GCS Application running from Version: {}\n'.format(
    #             os.environ['CURRENT_VERSION_ID']))
    #     self.response.write('Using bucket name: {}\n\n'.format(bucket_name))
    #
    # def create_file(self, filename):
    #     """Create a file."""
    #
    #     self.response.write('Creating file {}\n'.format(filename))
    #
    #     # The retry_params specified in the open call will override the default
    #     # retry params for this particular file handle.
    #     write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
    #     with cloudstorage.open(
    #             filename, 'w', content_type='text/plain', options={
    #                 'x-goog-meta-foo': 'foo', 'x-goog-meta-bar': 'bar'},
    #             retry_params=write_retry_params) as cloudstorage_file:
    #         cloudstorage_file.write('abcde\n')
    #         cloudstorage_file.write('f' * 1024 * 4 + '\n')
    #     self.tmp_filenames_to_clean_up.append(filename)

    @classmethod
    def upload_blob(cls, bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""

        # bucket_name = os.environ.get(
        #     bucket_name, app_identity.get_default_gcs_bucket_name())
        #
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('File {} uploaded to {}.'.format(
            source_file_name,
            destination_blob_name))
        # https: // storage.cloud.google.com / [BUCKET_NAME] / [OBJECT_NAME]
        print('-----------------------------------------------------------------------')
        print(blob.public_url)
        print('-----------------------------------------------------------------------')
        return blob.public_url
        # return 'https://storage.cloud.google.com/my-bucket/' + source_file_name

    @staticmethod
    def delete_blob(bucket_name, blob_name):
        """Deletes a blob from the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.delete()

        print('Blob {} deleted.'.format(blob_name))

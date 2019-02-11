# from beaker.ext import google
from google.cloud import storage


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

    @classmethod
    def upload_blob(cls, bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        cls.create_bucket(bucket_name)
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

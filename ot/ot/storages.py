from storages.backends.s3boto3 import S3Boto3Storage

#static과 media 파일을 구분해서 올린다.

class StaticS3Boto3Storage(S3Boto3Storage):
    location = 'static' # [static] bucket 업로드 prefix 지정

class MediaS3Boto3Storage(S3Boto3Storage):
    location = 'media' # [media] bucket 업로드 prefix 지정
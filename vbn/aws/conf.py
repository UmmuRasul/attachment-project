import datetime

AWS_ACCESS_KEY_ID = 'AKIA4PWLLXJ4N7QHTFNP'
AWS_SECRET_ACCESS_KEY = '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'

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =None

DEFAULT_FILE_STORAGE = 'vbn.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'vbn.aws.utils.StaticRootS3BotoStorage'

AWS_STORAGE_BUCKET_NAME = 'video-blogs-system'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
S3DIRECT_REGION = 'eu-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

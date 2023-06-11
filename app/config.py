import os
ENV = os.environ.get('APP_ENV', 'dev_local')

FLASK_DEBUG_PORT = 5000

if ENV in ('dev_local', 'dev_docker', 'stg'):
    if ENV in ('dev_local', 'stg'):
        PG_HOST = 'localhost'
    elif ENV == 'dev_docker':
        PG_HOST = 'db'

    PG_USER = 'hikma_dev'
    # PG_PASSWORD = 'password'
    PG_PASSWORD = '96DDDDDB6425'
    PG_DB = 'hikma_dev'
    FLASK_DEBUG = True
    PHOTOS_STORAGE_BUCKET = 'dev-api-photos'
    EXPORTS_STORAGE_BUCKET = 'dev-api-exports'
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = 'bd227f3d-0fbb-45c5-beed-8ce463481415'

if ENV == 'prod':
    FLASK_DEBUG = False
    PG_USER = 'hikma-prod-2'
    PG_PASSWORD = os.environ['DB_PASSWORD']
    PG_HOST = '10.127.208.3'
    PG_DB = 'hikma-prod-2'
    PHOTOS_STORAGE_BUCKET = os.environ['PHOTOS_STORAGE_BUCKET']
    EXPORTS_STORAGE_BUCKET = os.environ['EXPORTS_STORAGE_BUCKET']
    LOCAL_PHOTO_STORAGE_DIR = '/tmp/hikma_photos'
    DEFAULT_PROVIDER_ID_FOR_IMPORT = os.environ['DEFAULT_PROVIDER_ID']
    
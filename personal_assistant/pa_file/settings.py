from decouple import config


CLOUDINARY_STORAGE = {
    key: config(f'CLOUDINARY_{key}')
    for key in ('CLOUD_NAME', 'API_KEY', 'API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'

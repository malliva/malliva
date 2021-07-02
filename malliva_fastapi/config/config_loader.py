import os
import secrets

# get environment mode
environment_mode = os.getenv('MALLIVA_ENVIRONMENT', 'DEVELOPMENT')

if environment_mode == 'DEVELOPMENT':
    from config.environments.development_settings import settings
    print("Running in development mode!!!")
elif environment_mode == 'PRODUCTION':
    from config.environments.production_settings import settings
    settings.OPENAPI_URL = ''
    settings.SECRET_KEY = secrets.token_urlsafe(32)
    print("Running in production mode!!!")

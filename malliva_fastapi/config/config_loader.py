import os

# get environment mode
environment_mode = os.getenv('MALLIVA_ENVIRONMENT', 'DEVELOPMENT')

if environment_mode == 'DEVELOPMENT':
    from config.environments.development_settings import settings
    print("Running in development mode!!!")
elif environment_mode == 'PRODUCTION':
    from config.environments.development_settings import settings
    settings.openapi_url = ''
    print("Running in production mode!!!")

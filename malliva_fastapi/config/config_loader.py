import os

# get environment mode
environment_mode = os.getenv('MALLIVA_ENVIRONMENT', 'DEVELOPMENT')

if environment_mode == 'DEVELOPMENT':
    from config.environments.development_settings import Settings
    print("Running in development mode!!!")
elif environment_mode == 'PRODUCTION':
    from config.environments.development_settings import Settings
    print("Running in production mode!!!")

settings = Settings()

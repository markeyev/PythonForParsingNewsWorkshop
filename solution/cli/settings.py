import os

GRPC_PARSING_API_URL = os.getenv('PARSER_HOST', 'localhost') + ':50051'

print(GRPC_PARSING_API_URL)

PARSING_TIMEOUT = 20  # Seconds

PROJECTS = {
    'default': {
        'MONGODB_CONN': (os.getenv('MONGO_HOST', 'localhost'), 27017),
        'MONGODB_DBNAME': 'default',

        'SOURCES_LANGUAGE': 'en',
    }
}

CURRENT_PROJECT = os.getenv('PROJECT', 'default')

from fastapi import FastAPI

backend = FastAPI()

@backend.get('/')
def serve_frontend():
    return 'Front-end coming soon!'

@backend.post('/print')
def print():
    return 'Printing!'
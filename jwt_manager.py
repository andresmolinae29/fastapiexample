import jwt

def create_token(data: dict):
    token: str = jwt.encode(data, key="my_secret_key", algorithm='HS256').encode().decode('utf-8') ## variable de entorno del sistema - desayunos felices
    return token

def validate_token(token: str) -> dict:
    data: dict = jwt.decode(token, key="my_secret_key", algorithms=['HS256'])
    return data
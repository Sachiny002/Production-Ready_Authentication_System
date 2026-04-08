from flask_jwt_extended import create_access_token, create_refresh_token

def generate_tokens(user_id):
    access = create_access_token(identity=user_id)
    refresh = create_refresh_token(identity=user_id)
    return access, refresh

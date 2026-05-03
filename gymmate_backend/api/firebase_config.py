import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
import os

from gymmate_backend.settings import BASE_DIR

# Service account key file - Firebase Console se download karna hoga
cred = credentials.Certificate(os.path.join(BASE_DIR, "serviceAccountKey.json"))
firebase_admin.initialize_app(cred)

def verify_firebase_token(token):
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        return None
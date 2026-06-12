from django.contrib.auth import authenticate
from accounts.models import UserModel
from typing import Optional

def AuthenticateUserService(phone_number: str, password: str) -> Optional[UserModel]:
    user = authenticate(username=phone_number, password=password)
    
    if user is not None:
        return user
        
    return None
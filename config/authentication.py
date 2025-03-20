#own authentication class 
#should return user : this user is request.user
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User

#this is to practice where the user comes from
class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request): #request : without user it's with cookies , headers...
        print(request.META)
        username = request.headers.get('X_USERNAME')
        print(username)
        if not username: #not logged in
            return None
        try:
            user = User.objects.get(username=username) #logged in
            print(username)
            return (user,None) #this is rule using tuple and sending None
        except User.DoesNotExist: #attempting to log-in but failed
            raise AuthenticationFailed(f"No User {username}")
        # return super().authenticate(request)
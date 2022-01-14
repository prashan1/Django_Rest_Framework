from rest_framework.throttling import UserRateThrottle   

class CustomUserThrottle(UserRateThrottle):
    scope = 'userCustomRate'
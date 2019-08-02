from rest_framework.throttling import UserRateThrottle


class LoginRateThrottle(UserRateThrottle):
    scope = 'login'


class RegistRateThrottle(UserRateThrottle):
    scope = 'regist'






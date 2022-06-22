from django.contrib.auth.models import User

class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    '''
    The default ModelBackend authenticates users against the database using the user
    model of django.contrib.auth. This will suit most of your projects. However,
    you can create custom backends to authenticate your user against other sources,
    such as a Lightweight Directory Access Protocol (LDAP) directory or any
    other system
    '''
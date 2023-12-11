from django.contrib.auth import get_user_model
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.middleware import RemoteUserMiddleware, AuthenticationMiddleware
from account_handler.models import UserProfile
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class RemoteUserCustomMiddleware(RemoteUserMiddleware):
    def process_request(self, request):
        res = super(RemoteUserCustomMiddleware, self).process_request(request)

        # Configure from request
        def set_key(obj, key, valkey, valkey2):
            if valkey in request.META and getattr(obj, key) != request.META[valkey]:
                setattr(obj, key, request.META[valkey])
                set_key.changed = True

            if valkey2 in request.META and getattr(obj, key) != request.META[valkey2]:
                setattr(obj, key, request.META[valkey2])
                set_key.changed = True

        # Track changes
        set_key.changed = False

        # Update object
        user = request.user
        print(f'RemoteUserCustomMiddleware user :->:')
        if(user.is_authenticated):
            for field in user._meta.fields:
                field_name = field.name
                field_value = getattr(user, field_name)
                print(f"{field_name}: {field_value}")

        if request.user.is_authenticated:
            set_key(user, 'email', 'AUTHENTICATE_MAIL', 'OIDC_CLAIM_mail')
            set_key(user, 'first_name', 'AUTHENTICATE_GIVENNAME',
                    'OIDC_CLAIM_givenName')
            set_key(user, 'last_name', 'AUTHENTICATE_SN', 'OIDC_CLAIM_sn')

            if hasattr(request.user, 'userprofile'):
                profile = request.user.userprofile
            else:
                profile = UserProfile.objects.create(user=user)

            set_key(profile, 'roll_number',
                    'AUTHENTICATE_EMPLOYEENUMBER', 'OIDC_CLAIM_employeeNumber')
            set_key(profile, 'type', 'AUTHENTICATE_EMPLOYEETYPE',
                    'OIDC_CLAIM_employeeType')

            if set_key.changed:
                user.save()
                profile.save()

        return res

class RemoteUserCustomBackend(RemoteUserBackend):
    create_unknown_user = True


class CustomOIDCAB(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super(CustomOIDCAB, self).create_user(claims)

        user.first_name = claims.get('givenName', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        profile = UserProfile.objects.filter(user=user)

        if profile.exists():
            profile = UserProfile.objects.get(user=user)
            profile.roll_number = claims.get('uid', '')
            profile.type = claims.get('employeeType', '')
        else:
            profile = UserProfile.objects.create(user=user)
            profile.roll_number = claims.get('uid', '')
            profile.type = claims.get('employeeType', '')
        
        profile.save()

        user.userprofile = profile
        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('givenName', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        profile = UserProfile.objects.filter(user=user)

        if profile.exists():
            profile = UserProfile.objects.get(user=user)
            profile.roll_number = claims.get('uid', '')
            profile.type = claims.get('employeeType', '')
        else:
            profile = UserProfile.objects.create(user=user)
            profile.roll_number = claims.get('uid', '')
            profile.type = claims.get('employeeType', '')

        profile.save()

        user.userprofile = profile
        return user
    
    def filter_users_by_claims(self, claims):
        username = claims.get('uid')
        if not username:
            return self.UserModel.objects.none()

        try:
            User = get_user_model()
            user = User.objects.get(username=username)
            profile = UserProfile.objects.get(user=user)
            return [profile.user]

        except UserProfile.DoesNotExist:
            return self.UserModel.objects.none()

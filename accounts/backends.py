from django.contrib.auth import get_user_model
from django.contrib.auth.backends import RemoteUserBackend


class ShibbolethRemoteUserBackend(RemoteUserBackend):
    """
    Authenticate users from Shibboleth headers.
    Code based on https://github.com/Brown-University-Library/django-shibboleth-remoteuser
    """
    def searchPennDirectory(self, username, key):
        # TODO Poll Penn Directory to get missing information
        # User: first/last name and email
        # Student: major, school, display name
        bearer = ""
        token = ""
        headers = {
            "Authorization-Bearer": bearer,
            "Authorization-Token": token,
        }
        params = {
            "email": username,
            "affiliation": "STU"
        }
        response = get("https://esb.isc-seo.upenn.edu/8091/open_data/directory",
            params=params, headers=headers, timeout=30)
        if response.status_code == 200:
            response = response.json()

    def authenticate(self, request, remote_user, shibboleth_attributes):
        if not remote_user:
            return
        User = get_user_model()
        username = self.clean_username(remote_user)
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_unusable_password()
            for key, value in shibboleth_attributes.items():
                if value:
                    setattr(user, key, value)
                else:
                    setattr(user, key, searchPennDirectory(username, key))

            user.save()
            user = self.configure_user(user)

        return user if self.user_can_authenticate(user) else None
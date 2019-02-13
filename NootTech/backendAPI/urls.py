from django.conf.urls import url
from .views import ListUsers, errorVideoView, SettingsView

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# TODO: Implement the following API urls
# api/files - List all files that belong to a user
# api/file - Get info for a specific file, make it  Post request
# api/settings - Get or Update a user's settings
# api/list-reports - Get list of reports
# api/list-favourites-Get list of favourited files
# api/add-report - Add a report (even anonymously)
# api/add-favourites - Add to favourited files
# api/random-video - Get random error video , Random Video Done
# api/sub-domain - Get info for a subdomain and file

urlpatterns = format_suffix_patterns([
    url(r'^token/auth', obtain_jwt_token),
    url(r'^token/refresh', refresh_jwt_token),
    url(r'^token/verify', verify_jwt_token),
    url(r'^list-users', ListUsers.as_view(), name='TestView'),
    url(r'^error-videos', errorVideoView.as_view(), name='Error_Videos'),
    url(r'^settings', SettingsView.as_view(), name='View-Settings'),
])


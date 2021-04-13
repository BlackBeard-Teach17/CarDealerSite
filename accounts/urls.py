from django.conf.urls import url, re_path

from .views import (
    AccountHomeView,
    AccountEmailActivateView,
    UserDetailUpdateView
)

urlpatterns = [
    url(r'^$', AccountHomeView.as_view(), name='home'),
    url(r'details/$', UserDetailUpdateView.as_view(), name='user-update'),
    url(r'email/confirm/\(?<key>[0-9A-Za-z]+\)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    url(r'email/resend-activation/$', AccountEmailActivateView.as_view(),name='resend-activation'),
]

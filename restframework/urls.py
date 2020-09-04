from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.views.generic import TemplateView, RedirectView
# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Django REST API Boilerplate', url='/a-different-path')

# from django.urls import path, include
# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

### Social Login As Facebook
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter    

# class GithubLogin(SocialLoginView):
#     adapter_class = GitHubOAuth2Adapter
#     callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
#     client_class = OAuth2Client

urlpatterns = [
    # url(r'^$', schema_view),
    url(r'^admin/', admin.site.urls),
    path('api/v1/', include('myapi.urls')),
    path('api/v2/', include('myapi.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    # Registration are optional
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    #  url(r'^rest-auth/github/$', GitHubLogin.as_view(), name='github_login'),
    url(r'^account/', include('allauth.urls')),
     url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    # url(r'^docs/$', get_swagger_view(title='API Docs'), name='api_docs')
    # url(r'^$', schema_view),
]
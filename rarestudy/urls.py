from django.urls import path
from django.views.generic import TemplateView
from rarestudy.views import topView
from rarestudy.views import accountView
from rarestudy.views import articleView
from rarestudy.views import commentView

app_name = 'rarestudy'

urlpatterns = [
    # Top
    path('', topView.Top.as_view(), name='top'),
    # user
    path('profile/', accountView.ProfileView.as_view(), name='profile'),
    path('edit/<uuid:pk>/', accountView.EditView.as_view(), name='edit'),
    path('signup/', accountView.SignUpView.as_view(), name='signup'),
    path('delete_confirm', TemplateView.as_view(template_name='registration/delete_confirm.html'), name='delete-confirmation'),
    path('delete_complete', accountView.DeleteView.as_view(), name='delete-complete'),
    # article
    path('article/<uuid:pk>/', articleView.Detail.as_view(), name='article/detail'),
    path('article/add/', articleView.Add.as_view(), name='article/add'),
    path('article/edit/<uuid:pk>/', articleView.Edit.as_view(), name='article/edit'),
    # comment
    path('comment/add/<uuid:pk>/', commentView.Add.as_view(), name='comment/add'),
    path('comment/edit/<uuid:pk>/', commentView.Edit.as_view(), name='comment/edit'),
]
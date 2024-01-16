
from django.urls import path
from .views import (
    Createcommentview,
    Createlikeview,
)
urlpatterns = [

    path('comment/',  Createcommentview.as_view()),
    path('createlike/', Createlikeview.as_view())
]



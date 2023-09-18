
from django.urls import path
from .views import StoryListCreateView, UserPromptCreateView

urlpatterns = [
    path('stories/', StoryListCreateView.as_view(), name='story-list-create'),
    path('prompts/', UserPromptCreateView.as_view(), name='user-prompt-create'),
]

from attr import field
from .models import Posts, space, subscription, Comment
from django.forms import ModelForm


class SpaceCreateForm(ModelForm):
    class Meta:
        model = space
        fields = ["name", "tags", "image", "owner","About"]


class subscriptionCreateForm(ModelForm):
    class Meta:
        model = subscription
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment", "user", "username", "Space", "Post"]


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["Title", "Content", "user", "username", "Space", ]

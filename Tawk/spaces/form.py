from .models import Posts, space, subscription, Comment
from django.forms import ModelForm


class SpaceCreateForm(ModelForm):
    class Meta:
        model = space
        fields = ["name", "tags", "image", "owner", "About","secret_code"]


class subscriptionCreateForm(ModelForm):
    class Meta:
        model = subscription
        fields = ["name","space_id","user","slug","is_member","code"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment", "user", "username", "Space", "Post"]


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ["Title", "Content", "user", "username", "Space", ]

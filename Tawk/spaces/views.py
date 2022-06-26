from ast import Subscript
from django.http import HttpResponseRedirect
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from .form import CommentForm, SpaceCreateForm, subscriptionCreateForm, PostForm
# Create your views here.
from .models import space, subscription, Posts, Comment
from simple_search import search_filter


def remove(string):
    return string.replace(" ", "")


@login_required
def getSpaces(request):
    Space = subscription.objects.filter(user=request.user.id)
    Owned_Spaces = space.objects.filter(owner=request.user)
    return render(request, 'space/spaces.html', {'Spaces': Space, 'subscribed': 1, 'Owned_Spaces': Owned_Spaces})


@login_required
def Myspace(request):
    Space = space.objects.filter(owner=request.user)
    return render(request, 'space/spaces.html', {'Spaces': Space, 'subscribed': 0})


@login_required
def spaces(request, slug):
    Space = space.objects.get(slug=slug)
    id = Space.id
    code = Space.secret_code
    Content = Posts.objects.filter(Space=id)

    Present = subscription.objects.filter(slug=slug, user=request.user.id)
    isOwner = Space.owner == request.user
    print(Space.owner == request.user)
    if (Space.owner == request.user) or (len(Present) != 0 and Present[0].is_member):

        if request.method == "POST":

            Pform = PostForm(request.POST)

            if Pform.is_valid:
                post = Pform.save()
                return redirect('getSpaces')

        else:
            Pform = PostForm()
        return render(request, 'space/space_room.html', {'space': Space, 'Posts': Content, 'form': Pform, 'isOwner': isOwner})

    else:
        if request.method == "POST":

            form = subscriptionCreateForm(request.POST)
            #print(request.POST)
            #form.name=Space.name
            Recieved_Code = remove(request.POST['code'])
            form.code = Recieved_Code
            #print(form.name,form.code)
            if form.is_valid() and form.code == code:
                pace = form.save()
                return redirect(f'/space/{Space.slug}')

        #  else:

        else:
            form = subscriptionCreateForm()
        return render(request, 'space/space.html', {'space': Space, 'form': form, 'present': len(Present), 'Posts': Content})


@login_required
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    spaces = space.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'spaces': spaces,
    }
    return render(request, 'space/space.html', context)


@login_required
def CreateSpace(request):
    # form=""
    if request.method == "POST":
        form = SpaceCreateForm(request.POST)
        form.secret_code = remove(request.POST['secret_code'])

        if form.is_valid() and form.secret_code != "":
            Space = form.save()
            return (f'space/{Space.slug}/')

    else:
        form = SpaceCreateForm()
    return render(request, 'space/createSpace.html', {'form': form})


@login_required
def ApproveRequests(request, id):
    subs = subscription.objects.get(id=id)
    subs.is_member = True
    subs.save()


@login_required
def UpdateRequests(request):
    subs = subscription.objects.filter()


@login_required
def SinglePost(request, slug, pk):
    spaceval = space.objects.filter(slug=slug, owner=request.user.id)
    # print(len(spaceval))
    spaceid = -1

    if(len(spaceval) == 0):
        spaceval = get_object_or_404(
            subscription, slug=slug, user=request.user.id)
        spaceid = spaceval.space_id
    else:
        spaceid = spaceval[0].id
    Post = get_object_or_404(Posts, id=pk, Space=spaceid)
    Comments = Comment.objects.filter(Post=pk, Space=spaceid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        # form.Space=spaceid
        # form.Post=pk
        # form.username=request.user.username
        # form.user=request.user.id
        if form.is_valid():
            comm = form.save()
            # url=f"/space/{slug}/"
            # print(url)
            return HttpResponseRedirect(f'/space/{slug}/singlePost/{pk}/')
        else:
            print('asdasd')
            print(form.errors)

    else:
        form = CommentForm()
    return render(request, 'space/singlePost.html', {'Post': Post, 'Comments': Comments, 'form': form, 'space': spaceid})


# def ExploreSpaces(request):
#     Space = space.objects.all()
#     return render(request, 'space/explore.html', {'Spaces': Space})


@login_required
def EditSpace(request, slug):
    Space = get_object_or_404(space, slug=slug, owner=request.user)
    Inactive_Subscriptions = subscription.objects.filter(
        is_member=False, space_id=Space.id)
    Active_Subscriptions = subscription.objects.filter(
        is_member=True, space_id=Space.id)
    return render(request, 'space/EditSpace.html', {'Space': Space, 'Subscriptions': Inactive_Subscriptions, 'Members': Active_Subscriptions})


@login_required
def Search_Space(request):

    if request.method == "POST":
        print(request.POST)
        search_fields = ['^name', 'About', 'tags__name']
        query = request.POST['spaceName']
        Spaces = space.objects.filter(search_filter(search_fields, query))
        return render(request, 'space/join.html', {'Spaces': Spaces, 'search': True, 'query': query})
    return render(request, 'space/join.html', {'search': False})

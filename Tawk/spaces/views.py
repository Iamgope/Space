from django.http import HttpResponseRedirect
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from .form import CommentForm, SpaceCreateForm, subscriptionCreateForm, PostForm
# Create your views here.
from .models import space, subscription, Posts, Comment


@login_required
def getSpaces(request):
    Space = space.objects.all()
    print(Space)
    return render(request, 'space/spaces.html', {'Spaces': Space, })


@login_required
def spaces(request, slug):
    Space = space.objects.get(slug=slug)
    id = Space.id

    Content = Posts.objects.filter(Space=id)

    Present = subscription.objects.filter(slug=slug, user=request.user.id)

    if (Space.owner == request.user) or (len(Present) != 0 and Present[0].is_member):

        if request.method == "POST":

            Pform = PostForm(request.POST)

            if Pform.is_valid:
                post = Pform.save()
                return redirect('getSpaces')

        else:
            Pform = PostForm()
        return render(request, 'space/space_room.html', {'space': Space, 'Posts': Content, 'form': Pform})

    else:
        if request.method == "POST":
            form = subscriptionCreateForm(request.POST)
            if form.is_valid():
                pace = form.save()
                #print(pace, "s")
        #  else:

        else:
            form = subscriptionCreateForm()
        return render(request, 'space/space.html', {'space': Space, 'form': form, 'present': len(Present), 'Posts': Content})


@login_required
def Myspace(request):
    Space = subscription.objects.filter(user=request.user.id)
    print(Space)
    return render(request, 'space/spaces.html', {'Spaces': Space})


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
        if form.is_valid():
            space = form.save()
            print(space)

            # login(request,user)
            # return redirect('spaces')
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


def ExploreSpaces(request):
    Space = space.objects.all()
    return render(request,'space/explore.html',{'Spaces':Space})

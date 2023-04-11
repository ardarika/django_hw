from django.http import HttpResponse


def blogs(request):
    return HttpResponse('home page')


def about(request):
    return HttpResponse('about')


def comment(request):
    return HttpResponse('leave your comment')


def create(request):
    return HttpResponse('create your post')


def update(request):
    return HttpResponse('update')


def delete(request):
    return HttpResponse('delete')


def profile(request):
    return HttpResponse('profile')


def register(request):
    return HttpResponse('register')


def login(request):
    return HttpResponse('login')


def change_password(request):
    return HttpResponse('change_password')


def more(request):
    return HttpResponse('more text')

# qweqweqw
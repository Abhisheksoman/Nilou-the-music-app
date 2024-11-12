from django.shortcuts import render,redirect
from .models import Music,Album
from user.models import User
from django.contrib import messages
from django.db.models import Q

def start(request):
    albums = Album.objects.prefetch_related('music_set').all()
    return render(request, 'music/index.html', {'albums': albums})

def home(request):
    # Check if the user is logged in by verifying the session
    email = request.session.get('email')
    if email:
        try:
            # Retrieve the user based on the session email
            user = User.objects.get(email=email)
            # Prefetch related music for all albums
            albums = Album.objects.prefetch_related('music_set').all()
            context = {
                'user': user,
                'albums': albums,
            }
            return render(request, 'music/index.html', context)
        except User.DoesNotExist:
            # Handle case where user does not exist in the database
            messages.error(request, 'User does not exist')
            return redirect('login_view')
    else:
        # Redirect to login if session email is not set
        return redirect('login_view')

def search_songs(request):
    if 'email' in request.session:
        template_path = 'music/index.html'

        search_query = request.GET.get('q', None)

        if search_query:
            search_result = Music.objects.filter(
                Q(song_title__icontains=search_query) |
                Q(album__albumName__icontains=search_query) |
                Q(album__artist__artistName__icontains=search_query)
            ).distinct()
        else:
            search_result = Music.objects.all()

        context = {'search_result': search_result, 'search_query': search_query}
        return render(request, template_path, context)
    else:
        return redirect('/login')
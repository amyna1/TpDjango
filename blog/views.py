from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Poste
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
@method_decorator(login_required, name='dispatch')


@login_required
class MaVueProtegee(LoginRequiredMixin, TemplateView):
    template_name = 'post_list.html'

class PostCreate(CreateView,LoginRequiredMixin):
    model = Poste
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostList(ListView,LoginRequiredMixin):
    model = Poste
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView,LoginRequiredMixin):
    model = Poste
    template_name = 'post_detail.html'

class ModifyPost(UpdateView,LoginRequiredMixin):
    model = Poste
    template_name = 'modifpost.html'
    form_class = PostForm
    success_url = reverse_lazy('post-list')

class DeletePost(DeleteView,LoginRequiredMixin):
    model = Poste
    template_name = 'suppost.html'
    success_url = reverse_lazy('post-list')
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list.html')  # Redirigez l'utilisateur vers la page de base après la connexion réussie
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authentification de l'utilisateur
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)  # Utilisez l'utilisateur authentifié pour la connexion
                messages.success(request, f'Bienvenue, {username} ! Votre compte a été créé avec succès.')
                return redirect('')  # Redirigez l'utilisateur vers la page 'base'
            else:
                messages.error(request, 'Erreur lors de l\'authentification.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def home(request):
    context = {'val': "Home Menu"}
    return render(request, 'post_list.html', context)
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
def index(request):
    template = 'blog/post_list.html'
    blogs = Poste.objects.all()
    context = {'blogs': blogs}
    return render(request, template, context)


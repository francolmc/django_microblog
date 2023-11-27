from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from .models import Micropost
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CustomSignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = "/login"

class WallView(ListView):
    model = Micropost
    template_name = "wall.html"
    context_object_name = "micro_posts"
    ordering = ["-created_at"] # Orden desc
    queryset = Micropost.objects.all().order_by("-created_at") # Orden desc

class CreatePostView(LoginRequiredMixin, CreateView):
    login_required = True
    model = Micropost
    template_name = "create_post.html"
    fields = ["content"]
    success_url = "/"

    def form_valid(self, form):
        # Asigna el usuario actual al campo 'user' del MicroPost
        form.instance.user = self.request.user
        return super().form_valid(form)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import CustomUser


from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user'
    fields = ('username', 'email', 'first_name', 'last_name', 'age', )
    login_url = 'login'


from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import UserUpdateForm
from django.views.generic import CreateView, ListView, DetailView
from .models import Author, Book, Checkout
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def HomePageView(request):
    return render(request, 'library_app/home.html')

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    context_object_name = 'detail'
    queryset = Author.objects.all()

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    queryset = Book.objects.all()
    status = Checkout.objects.first()
   

    

class BookDetailView(DetailView):
    context_object_name = 'book'
    queryset = Book.objects.all()

# class AuthorBookListView(ListView):
#     template_name = 'books/books_by_author.html'
    
#     def get_queryset(self):
#         self.author = get_object_or_404(Author, name=self.kwargs['author'])
#         return Book.objects.filter(author=self.author)

# class Registration(CreateView):
#     form_class = NewUserForm
#     success_url = reverse_lazy('author_list')
#     template_name = 'accounts/register.html'

# # class Login(LoginView):
# #     template_name = 'accounts/login.html'
# #     success_url = reverse_lazy('author_list')

# def Login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         redirect ('author_list')
        
#     else:
#         print('Invalid Login Credentials')
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
    
        if u_form.is_valid():
            u_form.save()
          
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        


    context = {
        'u_form': u_form,
        
    }
    return render(request, 'library_app/profile.html', context)


class CheckoutListView(ListView):
    model = Checkout
    template_name = 'library_app/checkout_list.html'
    context_object_name = 'checkouts'
    queryset = Checkout.objects.all()
    



    
    
    
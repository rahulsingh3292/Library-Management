from django.shortcuts import render,redirect
from django.contrib.auth import (login,authenticate,logout)
from django.http import JsonResponse
from datetime import timedelta 
from django.contrib import messages
from django.utils import timezone
from  .models import * 
from django.views.generic import (TemplateView,CreateView,UpdateView,ListView)
from  .forms import * 
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import AnonymousRequiredMixin
from .extras import * 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.. 

class SignUpView(AnonymousRequiredMixin,TemplateView):
  template_name = "accounts/signup.html"
  authenticated_redirect_url = "/"
 
  def post(self,request):
    first_name = request.POST.get("first_name")
    email = self.request.POST.get("email")
    password = self.request.POST.get("password")
    ac_type = self.request.POST.get("ac_type")
    if  User.objects.filter(email=email).exists():
      
      return JsonResponse({"status":False})
    
    user = User.objects.create_user(email=email,password=password)
    user.first_name = first_name
    user.is_active = False 
    if ac_type == "admin":
      user.requested_admin_ac = True 
    user.save()
    registration_success(email)
    return JsonResponse({"status":True})
    


@csrf_exempt
def activate_account(request):
  if request.method == "POST":
    email = request.POST.get("email")
    user = User.objects.filter(email=email).first()
    if user.is_active == False:
        user.is_active = True 
        user.save()
        BorrowedBook.objects.create(user=user)
        account_activated(email,user.first_name)
        return JsonResponse({"activated":True})
    else:
      return JsonResponse({"activated":False})
  
  return render(request,"accounts/activate.html")

 
class LoginView(AnonymousRequiredMixin,TemplateView):
  template_name = "accounts/login.html"
  authenticated_redirect_url ="/"
 
  def post(self,request):
    redirect_url = self.request.POST.get("next")
    email = self.request.POST.get("email")
    password = self.request.POST.get("password")
    
    user = authenticate(self.request,email=email,password=password)
 
    if user is not None:

      login(self.request,user)
      if redirect_url:
        return JsonResponse({"redirect_to":redirect_url})
      return JsonResponse({"login":True})
    return JsonResponse({"login":False})
    
@csrf_exempt
def logout_user(request):
  if request.method == "POST":
    logout(request)
    return redirect("/")

class HomeView(TemplateView):
  template_name = "library/home.html"
  def get_context_data(self,*args,**kwargs):
   
    books = Book.objects.all()

    context = {"books":books} 
    return context 
        
  def post(self,request):
    id = request.POST.get("book_id")
    book = Book.objects.get(id=id)
    borrow_user = BorrowRequest.objects.create(user=request.user,book=book)
    return JsonResponse({"status":True})

def update_book_html(request):
  categories = Category.objects.all()
  return render(request,"library/update_book.html",{"categories":categories})
  
class AddCategoryView(LoginRequiredMixin,CreateView):
  login_url = "/accounts/login/"
  model = Category 
  fields = ["title"]
  success_url = "/library/add/"
 
  def form_valid(self,form):
    super().form_valid(form)
    cat = Category.objects.latest("id")
    
    return JsonResponse({"status":True,"cat":[cat.id,cat.title]})
  
  def dispatch(self,request,*args,**kwargs):
    if not self.template_name:
      return redirect("addbook")
    return super().dispatch(request,*args,**kwargs)
  
  
class AddBookView(CreateView):
  form_class = AddBookForm
  success_url = "/library/addbook/"
  template_name = "library/addbook.html"
  
  def form_valid(self,form):
    super().form_valid(form)
    return JsonResponse({"status":True})
    
    
  def get_context_data( self, **kwargs):
    categories = Category.objects.all()
    context ={"categories":categories}
    return context
  
  def dispatch(self,request,*args,**kwargs):
    if not request.user.is_authenticated:
      return redirect("/accounts/login?next=/library/addbook/")
    elif not request.user.is_admin_user:
      return redirect("/")
    
    return super().dispatch(request,*args,**kwargs)
  
    
  
class UpdateBookView(UpdateView):
  form_class = AddBookForm 
  model = Book
  pk_url_kwarg = 'id'
  
  def get_context_data(self,*args,**kwargs):
    books = Book.objects.all()
    context = {"books":books}
    return context
    
  def form_valid(self,form):
    super().form_valid(form)
    return JsonResponse({"updated":True})

  def get_object(self,**kwargs):
    id = self.kwargs.get("id")
    book = self.model.objects.filter(id=id)
    if book.exists():
      return book.first()
    return book
  def get_success_url(self,**kwargs):
    return f"/library/update/{self.kwargs.get('id')}/"
  
  
  def dispatch (self,request,*args,**kwargs):
    if not request.user.is_authenticated:
      return redirect("/accounts/login?next=/library/addbook/")
    elif not request.user.is_admin_user:
      return redirect ("/")
      
    return super().dispatch(request,*args,**kwargs)
  

def search_book(request):
  book_id = request.GET.get("book_id")
  res = None
  if not book_id:
    return JsonResponse({"book":res})
  book = Book.objects.filter(id=book_id)
  if book.exists():
    book = book.first()
    res = {"book_name":book.book_name,"author":book.author,"cat_id":book.category.id}
  return JsonResponse({"book":res})


def ajax_books(request):
  books = [[i.book_name,i.id] for i in Book.objects.all()]
  return JsonResponse({"books":books})



class MyBookView(LoginRequiredMixin,ListView):
  login_url = "/accounts/login/"
  model = BorrowedBook
  template_name = "library/my_books.html"
  
  def get_queryset(self,*args,**kwargs):
    return self.model.objects.get(user=self.request.user).books.all()

  
def return_book(request):
  if request.method == "POST":
    book_id = request.POST.get("book_id")
    book = Book.objects.get(id=book_id)
    my_books = BorrowedBook.objects.get(user=request.user)
    if my_books.books.filter(id=book_id).exists():
      my_books.books.remove(book)
      my_books.save()
      book.available = True 
      book.save()
    return JsonResponse({"returned":True})

    
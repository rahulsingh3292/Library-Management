from django.urls import path 
from  .import views 

urlpatterns = [
  
    path("",views.HomeView.as_view(),name="home"),
    
    path("accounts/signup/",views.SignUpView.as_view(),name="signup"),
    
    path("accounts/login/",views.LoginView.as_view(),name="login"),
    
    path("accounts/logout/",views.logout_user,name="logout"),
    
    path("accounts/activate/",views.activate_account,name="activate_account"),
    
    path("library/add_category/",views.AddCategoryView.as_view(),name="add_category"),

    path("library/update_book/",views.update_book_html,name="update_book"),
    
    path("library/update/<int:id>/",views.UpdateBookView.as_view(),name="update_book"),
    
    path("library/search_book/",views.search_book,name="search_book"),
   
    path("library/addbook/",views.AddBookView.as_view(),name="addbook"),
    
    path("library/books/",views.ajax_books),
    
    path("library/my_books/", views.MyBookView.as_view(),name="my_books"),
    
    path("library/return_book/",views.return_book,name="return_book")
  ]
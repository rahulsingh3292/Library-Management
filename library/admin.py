from django.contrib import admin
from  .models import * 
# Register your models here.

@admin.register(Category)
class CategoryAdmib(admin.ModelAdmin):
  list_display = ["title"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ["id","book_name","author","category","added_on","image"]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display =["id","email","first_name","last_name","is_active" ,"requested_admin_ac","is_admin_user"]
  
@admin.register(BorrowRequest)
class BorrowRequestbookAdmin(admin.ModelAdmin):
  list_display =["id","user","book","verified"]

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
  list_display =["id","user"]
  
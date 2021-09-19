from django.dispatch import receiver 
from django.db.models.signals import post_save 
from  .models import User ,BorrowRequest,BorrowedBook,Book
from  .extras import admin_account_activated,borrow_success

@receiver(post_save,sender=User)
def admin_account_activate(sender,instance,created,**kwargs):
  if not created:
    if instance.is_admin_user == True:
      admin_account_activated(instance.email,instance.first_name)

@receiver(post_save,sender=BorrowRequest)
def requested_borrow_book(sender,instance,created,**kwargs):
  if not created:
    if instance.verified == True :
      model = BorrowedBook.objects.get(user=instance.user)
      model.books.add(instance.book)
      borrow_success(instance.user.email,instance.user.first_name,instance.book.book_name)
  else:
    book = Book.objects.get(id=instance.book.id)
    book.available = False 
    book.save()


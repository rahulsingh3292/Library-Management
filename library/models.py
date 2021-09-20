from django.db import models
from  .managers import User 
# Create your models here.

class Category (models.Model):
  title = models.CharField(max_length=200)
  
  def __str__(self):
    return self.title 
 
class Book(models.Model):
  book_name = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="cats")
  available = models.BooleanField(default=True)
  image = models.ImageField(upload_to="/book_images",blank=True, default="/media/book_image.jpg")
  added_on = models.DateTimeField(auto_now_add=True, blank=True)
  
  def __str__(self):
    return self.book_name
    
class BorrowedBook(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  books = models.ManyToManyField(Book,related_name="borrowed_books",blank=True)
  
  def __str__(self):
    return str(self.user.email)

class BorrowRequest(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  book = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
  verified = models.BooleanField(default=False)
  
  def __str__(self):
    return self.book.book_name
  
  
  
  

  
 
  
  
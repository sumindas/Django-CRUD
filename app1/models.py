from django.db import models

# Create your models here.

class destination(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    


    def __init__(self):
        return self.name
    

class Student(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email = models.EmailField()
    
class author(models.Model):
    author_name = models.CharField(max_length=50,null=True)
    author_id = models.IntegerField()
    
    def __str__(self):
        return self.author_name   
    
class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    auth_name = models.ForeignKey(author,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title

    
     
class Song(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class students(models.Model):
    nameofstudent = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    mark_out_of_100 = models.IntegerField()
    
    def __str__(self):
        return self.nameofstudent


class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    
    def _str_(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def _str_(self) -> str:
        return self.name
    
    
# class Subproduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     prouct_name = models.CharField(max_length=60)
    
#     def _str_(self) -> str:
#         return self.product.name
    

    
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name


class Article(models.Model):
    blog = models.ForeignKey(Author, on_delete=models.CASCADE) ##if we delete an Author, all articles associated with that author will get deleted. 
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 500)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
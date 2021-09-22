from django.db import models

class Todo(models.Model):
  desc = models.CharField(max_length = 500)
  date_create = models.DateTimeField(auto_now=False, auto_now_add=True)
  date_complete = models.DateTimeField(null=True)
  flag_complete = models.BooleanField()
  def __str__(self):
    return self.desc





# Let's create a simple todo app. This can be done with a single model TodoItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed. The user should be presented with an input field and a button (in a form). When the clicks the button, it should save the data to the server and show the newly-added item in the list

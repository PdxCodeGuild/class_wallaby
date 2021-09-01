This guide covers the content in the folder **Forms and Links**.
## How to use a model and a database inside your template

Before continuing further, add new URLs in the my_app > urls.py folder:

```python
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('add/', views.add_blog_post, name = 'add_posts'),
    path('register/', views.register_author, name = 'register_author'),
    path('view_all/', views.view_all, name = 'view_all')
    ]
```

- Go to the my_app folder > views.py, import both models and add new views:

```python
from django.shortcuts import render, redirect
from .models import Author, Article


""" This function allows to register a new author and the form in the
register.html page is linked to it. 
"""
def register_author(request): ##if you visit the register/ url, simply render the template
    if request.method == 'GET': 
        return render(request, 'pages/register.html')
    elif request.method == 'POST': ## if you interact with the form on the html page, then get the input from the form and create an instance of the Author class in the database.
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']    
        email = request.POST['email']
        Author.objects.create(first_name = first_name, last_name = last_name, email = email)
        return redirect('add_posts')

"""
This function allows you to create a new Article object in the database.
"""
def add_blog_post(request):
    authors = Author.objects.all() ## returns a list of Authors
    context = {'authors': authors} 
    if request.method == 'GET':
        return render(request, 'pages/add_blog_post.html', context) ##passing the list of authors to the page
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = request.POST['author']
        result = Author.objects.get(id = author)
        Article.objects.create(author = result, title = title, text = text, pub_date = pub_date)
        return redirect('view_all')

"""
This function returns a list of articles that exist in the database
"""
def view_all(request):
  authors = Author.objects.all()## This queries the database, and saves a list of authors in the variable 'authors'
  return render(request, 'pages/all.html', {'authors': authors}) ##passing the list to the page all.html.

   
```
## Add a form to register a new Author.

- In the Pages folder create a new page `register.html` and add the following:

```html
{% extends 'base.html' %} {% block content %}

<div class="container mt-5">
  <form action="{% url 'register_author' %}" method="POST">
    {% csrf_token %}
    <div class="form-group">
      <label for="first_name">First Name</label>
      <input
        type="text"
        name="first_name"
        class="form-control"
        placeholder="First Name"
      />
    </div>
    <div class="form-group">
      <label for="last_name">Last Name</label>
      <input
        type="text"
        name="last_name"
        class="form-control"
        placeholder="Last Name"
      />
    </div>
    <div class="form-group">
      <label for="email">Email address</label>
      <input
        type="email"
        name="email"
        class="form-control"
        aria-describedby="emailHelp"
        placeholder="Enter email"
      />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</div>
{% endblock %}
```
This page is linked to the `register_author` function and it simply allows you to create a new Author instance in the database.

## Add a form to create blog posts.

- In the Pages folder create a new page `add_blog_post.html` and add the following:

```html
{% extends 'base.html' %} {% block content %}

<div class="container mt-5">
  <form class="mt-3" action="{%url 'add_posts' %}" method="POST">
    {% csrf_token %}
    <div id="author-form" class="form-group">
      <label for="book_title">Article Title</label>
      <input
        type="text"
        class="form-control"
        name="title"
        placeholder="enter the article title"
      /></br>
      <textarea
        class="form-control"
        rows="3"
        name="text"
        placeholder="article main text"
      ></textarea></br>
      <input
        type="date"
        class="form-control"
        name="pub_date"
        value="2018-07-22"
        min="2018-01-01"
        max="2030-12-31"
      /><br />
      {%if authors%} 
      <select class="form-control" name="author">
        {%for author in authors%}
        <option value="{{author.id}}">{{author}}</option>
        {% endfor %}
      </select>
      <button type="submit" class="btn btn-primary mb-2 mt-3">Submit</button>
      {%else%}
      <a class="nav-link" href="{% url 'register_author'%}"
        >Register an author first!</a
      >
      {%endif%}
    </div>
  </form>
</div>
{% endblock %}
```
## Add a page where you can display all the articles.

- In the Pages folder create a new page `all.html` and add the following:

```html

{% extends 'base.html' %} {% block content %}

<div class="container mt-5">
  <h1>Your articles</h1>
  {%for person in authors%} 
    {%for post in person.article_set.all%}
  <ul class="list-group mt-4">
    <li class="list-group-item">{{person.first_name}}</li>
    <li class="list-group-item">{{post.title}}</li>
    <li class="list-group-item">{{post.text}}</li>
    <li class="list-group-item">{{post.pub_date}}</li>
  </ul>
    {% endfor %} 
  {% endfor %}
</div>
{% endblock %}
```
This is an important step. We are passing a list of authors to the page, but at the same time we are querying the database and displaying a list of articles associated to each author thanks to `_set.all`. 

To clarify, we run the first loop to iterate through all authors, then we go one level deeper and we run an additional nested loop that returns all articles linked to each author. You can read more about sets [here](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/)

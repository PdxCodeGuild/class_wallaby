## Create a reverse view

Let's create a view that displays a specific article. This view requires you to add a `<int:id>` in the URL. First of all, in the _my_app > urls.py page add:

```python
  path('post_details/<int:id>', views.post_details, name = 'details'),
```

The entire page should now look like this:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('add/', views.add_blog_post, name = 'add_posts'),
    path('register/', views.register_author, name = 'register_author'),
    path('view_all/', views.view_all, name = 'view_all'),
    path('post_details/<int:id>', views.post_details, name = 'details'),
    ]
```

- Inside your app folder > views.py add a view to return a page based on the ID of the element we are targeting:

```python
def post_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    post = Article.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/post_details.html', {"post": post}) ## we are passing the context to the page
```

- Update the Templates > Pages > all.html to look like the following:

```html
{% extends 'base.html' %} {% block content %}
<div class="container mt-5">
  <h1>Your articles</h1>
  {%for person in authors%} 
    {%for post in person.article_set.all%}
    <ul class="list-group mt-4">
      <li class="list-group-item">{{person.first_name}}</li>
      <li class="list-group-item">
        <a href="{% url 'details' post.id%}">{{post.title}}</a>
      </li>
      <li class="list-group-item">{{post.text}}</li>
      <li class="list-group-item">{{post.pub_date}}</li>
    </ul>
    {% endfor %} 
  {% endfor %}
</div>
{% endblock %}

```

As you can see we added an <a> tag with a link to a page that is served by the view we just added.

- Now we need to add a page that displays just an article. In the Pages folder, add a `post_details.html` page:

```html
{% extends 'base.html' %} {% block content %}
<div class="container mt-5">
  <a href="{% url 'view_all'%}"><h3>Back to all articles</h3></a>
  <ul>
    <p>ID: {{ post.id }}</p>
    <p>Description: {{ post.text }}</p>
    <p>Pub Date: {{post.pub_date}}</p>
  </ul>
</div>
{% endblock %}

```
## Different types of routing in DRF

### Introduction
The Django REST framework provides different ways of URL mapping or routing in an API project. Besides the traditional style of routing, there are other routing techniques that can save you time while developing. In this reading, you are going to learn about both traditional and other techniques.

Note: All the routings should be done in the urls.py file in your Django app.

### Regular routes
The code below maps a function from a views.py file to an API endpoint. Don’t forget that you have to import the path function from the django.urls module first.
```py
from django.urls import path
from . import views
urlpatterns = [
	path('books’,views.books),
]
```
This URL pattern maps the books function to the /api/books endpoint. You already know how to specify which HTTP methods a function view can serve by supplying them in the api_decorator function. The following code allows any function view to serve both HTTP GET and POST methods.
```py
@api_view([‘GET’,’POST’])
```

### Routing to a class method
If you map a specific method from a class, then you need to declare that method as a @staticmethod first. After that, you can map it in the urls.py file. Here’s an example of a class in the views.py file.
```py
class Orders():
	@staticmethod
	@api_view()
	def listOrders(request):
    	return Response({'message':'list of orders'}, 200)

```
You can also map this listOrders method in the urls.py file as follows.  
```py
from django.urls import path
from . import views
urlpatterns = [
	path('orders', views.Orders.listOrders)
]
```

### Routing class-based views
You can save a lot of time in DRF by mapping a class that extends the APIview. You don’t need to individually map every method of such classes. In an upcoming video, Function and class-based views, you will learn that such classes have HTTP verb-specific methods inside them. When a class extends APIview or generic views, you can simply map those classes in the urls.py file.

Here’s the code of the class that extends the APIView.
```py
class BookView(APIView):
	def get(self, request, pk):
    	return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
	def put(self, request, pk):
    	return Response({"title":request.data.get('title')}, status.HTTP_200_OK)
```
And here is how you map this class in the urls.py file. All you have to do is map the class as a viewagainst an endpoint.  
```py
from django.urls import path
from . import views
urlpatterns = [
    path('books/<int:pk>',views.BookView.as_view())
]
```
Now you can make HTTP, GET and PUT calls to the /api/books/{bookId} endpoint without issues. If the class has post(), delete() and patch() methods, it will work with HTTP POST, DELETE and PATCH methods too.

### Routing classes that extend viewsets
You can have classes that extend the different types of ViewSets in your API project. Just like the classes that extend APIView, these classes also have specific methods used to respond to different types of HTTP requests. Here’s an example of a typical class that extends the viewset.Viewset class.
```py
Class BookView(viewsets.ViewSet):
	def list(self, request):
    	return Response({"message":"All books"}, status.HTTP_200_OK)
	def create(self, request):
    	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
	def update(self, request, pk=None):
    	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
	def retrieve(self, request, pk=None):
    	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
	def partial_update(self, request, pk=None):
        return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
	def destroy(self, request, pk=None):
    	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
```
You can map this class in the urls.py file in your Django app as follows.
```py
urlpatterns = [
	path('books', views.BookView.as_view(
    	{
        	'get': 'list',
        	'post': 'create',
    	})
	),
    path('books/<int:pk>',views.BookView.as_view(
    	{
        	'get': 'retrieve',
        	'put': 'update',
        	'patch': 'partial_update',
        	'delete': 'destroy',
    	})
	)
]
```
Notice how the HTTP verbs are mapped with each method in this class. Also, note that both the list() and retrieve() methods are present. The list() method is used to display all books, and the retrieve() method is used to display a single book.

After this mapping, you can access the  http://127.0.0.1:8000/api/books  endpoint with GET and POST methods. While you can access the http://127.0.0.1:8000/api/books/1  endpoint with GET, PUT, PATCH and DELETE.

### Routing with SimpleRouter class in DRF
If you have a class that extends ViewSets then you can use different types of built-in routers to map those classes in your urls.py file. Doing things this way means you don’t have to map the individual methods as you did in the previous section. Initiate a SimpleRouter object and map the class in the urls.py file in your Django app as follows.
```py
from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```
After mapping, you can access the api/books and api/books/1 endpoints with the same methods as in the previous example.      

Did you notice that the argument trailing_slash=False was passed, instantiating the SimpleRouter object? Without this argument, your API endpoints will have a trailing slash. And, since you don’t want a trailing slash at the end of your API endpoints, you have to pass this argument. 

## Routing with DefaultRouter class in DRF
There is another type of router called DefaultRouter which provides an extra benefit over the SimpleRouter. It creates an API root endpoint with a trailing slash that displays all your API endpoints in one place. You can use it this way in the urls.py file. 
```py
from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash=False)
router.register('books', views.BookView, basename='books')
urlpatterns = router.urls
```
Again, after mapping, you can access the api/books and api/books/1 endpoints with the same methods as in the previous examples.

Additionally, you can access the API root view when you visit the http://127.0.0.1:8000/api/ endpoint.

## Generic views and ViewSets in DRF

### Introduction
DRF comes with many generic views and ViewSet to speed up API development. When you use these classes, you don’t need to start from scratch and using them will reduce the code in your API project. In this reading, you will learn about different types of generic views and ViewSet as well as their purposes and benefits. 

### ViewSets
ViewSets are simple class-based views, but they come with benefits. There are a few ViewSets classes available in DRF that you can use to quickly scaffold a functioning API CRUD project. You can also provide permission classes and throttle classes to allow authenticated API calls and rate limiting.

To use these classes, you must import the viewsets module from the rest_framework:  
```py
from rest_framework import viewsets
```

#### ViewSet
There are a few ViewSet classes but the foundation is ViewSet and it extends the APIView. When your class-based views extend a ViewSet you get browsable API views out of the box. Except for that, every ViewSet comes with a method naming convention for easier one-line routing that saves a lot of time. 

When a ViewSet is used to deal with a collection of resources, you can write your business logic in list() and create() methods inside this class. 
|Class Method|Supported HTTP Method|Purpose|
|-|-|-|
|list()|GET|Display resource collection|
|create()|POST|Create new resource|

You can use the following methods to write the business logic when a ViewSet deals with a single resource.

|Class Method|Supported HTTP Method|Purpose|
|-|-|-|
|retrieve()|GET|Display a single resource|
|update()|PUT|Completely replace a single resource with new data|
|partial_update()|PATCH|Partially update a single resource|
|destroy|DELETE|Delete a single resource|

When you extend a ViewSet, you will have to manually write code to perform the database operations. But there are two more ViewSet classes that can automatically do that for you. This is how you extend a ViewSet class.

```py
class MenuItemViewSet (viewsets.ViewSet)
```

### ModelViewSet
If the class-based view extends a ModelViewSet, it can automatically handle CRUD operations for you. All you must do is give this class a queryset and a serializer, and everything else will be done automatically.  You don’t need to write code for all those database operations anymore. Later in this course, you will see a practical example of using ModelViewSet to write a functioning CRUD API project with only a few lines of code. Here’s an example of how to extend this ViewSet.
```py
class MenuItemView (viewsets.ModelViewSet)
```

### ReadOnlyModelViewSet
As the name suggests, when your class-based views extend a ReadOnlyModelViewSet, it can only display a single resource and resource collection. No write-operation is allowed by such views, so it doesn’t handle POST, PUT, PATCH or DELETE methods.  Here’s an example of extending a ReadOnlyModelViewSet.

```py
class ReadOnlyMenuItemView (viewsets.ReadOnlyModelViewSet)
```

### Generic views
Generic views are another way of quickly writing class-based views to scaffold fully functional CRUD API projects. There are several generic views that offer a particular functionality, like displaying resources or creating a new resource and so on. All you must do is extend these generic views to make your API endpoints work. 

To use these generic view classes, you must import the generics module from the rest_framework.
```py
from rest_framework import generics
```

All generic view classes require a queryset and a serializer to work properly. 

Here is a list of generic views in DRF and their purposes.
|Generic view class|Supported method|Purpose|
|-|-|-|
|CreateAPIView|POST|Create a new resource|
|ListAPIView|GET|Display resource collection|
|RetrieveAPIView|GET|Display a single resource|
|DestroyAPIView|DELETE|Delete a single resource|
|UpdateAPIView|PUT and PATCH|Replace or partially update a single resource|
|ListCreateAPIView|GET and POST|Display resource collection and create a new resource|
|RetrieveUpdateAPIView|GET, PUT, PATCH| Display a single resource and replace or partially update it|
|RetrieveDestroyAPIView|GET, DELETE|Display a single resource and delete it|
|RetrieveUpdateDestroyAPIView|GET, PUT, PATCH, DELETE|Display, replace or update and delete a single resource|

#### Example Code
If you want API endpoints to be capable of displaying resource collection and creating a new resource, you have to extend both ListAPIView and CreateAPIView, or just ListCreateAPIView. Both of the following lines of code do the same job.
```py
class MenuItemView (generics.ListAPIView, generics.CreateAPIView)
```
```py
class MenuItemView (generics.ListCreateAPIView)
```
Just like ModelViewSet, you must give these generic view classes a queryset and a serializer and you don’t need to manually write code to perform these database operations. 

### Authentication and selective authentication
If you want all API calls to be authenticated in a class-based view that extends the generic views, you can add the permission_classes public attribute in the class. 

```py
Permission_classes = [IsAuthenticated]
```

If you want to selectively enable authentication for some calls, like POST, PUT, PATCH and DELETE then you need to override the get_permission method in your class-based view like this.

```py
def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
            
        return [permission() for permission in permission_classes]
```

This way, anyone will be able to make GET call, but other HTTP methods like POST, PUT, PATCH and DELETE will require authentication or a valid user token.

#### Return items for the authenticated user only 
Sometimes in a class-based view that extends a generic view, you may want to return resources created by the authenticated users only. In that case, you need to override the get_queryset method. The following code in a class-based view returns only those orders created by the authenticated user. 
```py
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Order.objects.all().filter(user=self.request.user)
```

#### Override default behavior 
Though generic views automate everything, you still have full scope to change the default behavior by overriding any of the default methods. Here is an example that returns a simple static response instead of the resources. 
```py
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    def get(self, request, *args, **kwargs):
        return Response(‘new response’)
```
The other methods you can override are post(), put(), patch() and delete().

## M2: Other Types of Serializers in DRF

### Introduction
You now know about serializers in DRF and you learned how to use model serializers to serialize model relationships. This reading has some interesting tips and tricks regarding serialization, like how to automatically display a nested model field using the depth option of the serializer. You will also learn how to display related model fields as hyperlinks by using the HyperlinkedRelatedField or by using a new type of serializer called the HyperlinkedModelSerializer. 

### Nested fields
If you were to visit the menu-items endpoint, you would note the category displays as a nested field with its id, title, and slug. 
```json
    {
        "id": 1,
        "title": "Sample",
        "price": "1.00",
        "stock": 1,
        "price_after_tax": 1.1,
        "category": {
            "id": 1,
            "slug": "icecream",
            "title": "icecream"
        }
    }
```
This can be achieved in two ways.

**Method 1**
The first way to do this is to create a category serializer in serializers.py and include it in the menu item serializer as demonstrated in the code below. 
```py
from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category 
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']
 
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

**Method 2**
There is another way of doing this. Instead of declaring the category field as CategorySerializer you can specify that depth=1 is in the Meta class in MenuItemSerializer. This way, all relationships in this serializer will display every field related to that model.  You can change the code of the MenuItemSerializer as below. 
```py
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
        depth = 1
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```
Note the commented line, category = CategorySerializer(). And the new line, depth = 1, was added in the Meta class. Now, if you were to visit the menu items endpoint at http://127.0.0.1:8000/api/menu-items you’d note that the output is exactly the same as it was before. 

Displaying nested fields this way provides more information. It also reduces the amount of code the client application developers need to write. This is because they don't have to make separate API calls to retrieve the details for those nested fields anymore.

Next, let’s focus on different serialization techniques that you can use to display related model fields as hyperlinks.

#### Display a related model fields field as a hyperlink 
In DRF you can display every related model field as a hyperlink in the API output. Like this:  http://127.0.0.1:8000/api/category/{categoryId}  for the category field. There are two different ways to do this. The first method is to use the serializer field called HyperlinkedRelatedField and for the second method you use the HyperlinkedModelSerializer.

**Method 1: HyperlinkedRelatedField**

Step 1: Create and map a new view function 

Every HyperlinkedRelatedField field in a serializer needs a queryset to find the related object and a view name that is used to map the hyperlinked URL pattern.

Thus you have to create a new function in the views.py file that will handle the categoryId endpoints. 
```py
from .models import Category from .serializers import CategorySerializer
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data) 
```
Then you map this function in the urls.py file with a view name. 
```py
path('category/<int:pk>',views.category_detail, name='category-detail')
```
Tip: There is a convention you must follow when you create this view name. The rule is that you have to add -detail after the related field name, which is category in the MenuItemSerializer. This is why the view name was category-detail in this code. If the related field name was user, the view name would be user-detail. 

Step 2: Create a HyperLinkedRelatedField in the serializer

The next step is to change the MenuItemSerializer code. The following code sets the category field as a HyperLinkedRelatedField in the MenuItem serializer.
```py
from .models import Category
class MenuItemSerializer(serializers.ModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name='category-detail'
    )
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```
Note how a queryset and a view name are provided in the category HyperlinkedRelatedField. The code follows the convention so you can remove the line, view_name='category-detail. It is only necessary if you didn’t follow the convention and you created the view name in a different way in the urls.py file. 

Step 3: Add context

The final step is to add context to the MenuItemSerializer in the menu_items function, as below.
```py
serialized_item = MenuItemSerializer(items, many=True, context={'request': request})
```
Note: The argument context={'request': request} lets the menu-items endpoint display the category field as a hyperlink.
```py
    {
        "id": 1,
        "title": "Sample",
        "price": "1.00",
        "stock": 1,
        "price_after_tax": 1.1,
        "category": "http://localhost:8000/api/category/1"
    }
```	
You can click on that hyperlink and check the category details. 

**Method 2: HyperlinkedModelSerializer**
But there is another way to display a category field as a hyperlink. With this method, you need to change the code in the serializers.py file. so that the MenuItemSerializer extends the serializers.HyperlinkedModelSerializer class instead of the serializers.ModelSerializer class.
```py
class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock =  serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')
 
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock', 'price_after_tax','category']
    
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```
When you use the HyperlinkedModelSerializer the output of the menu-items endpoint produces the same output with a hyperlinked category field like in the screenshot in Method 1 but the code is much cleaner and simpler.

Note: When you use a HyperlinkedModelSerializer, you still need the URL pattern with a view name as you did in the previous section. 
```py
urlpatterns = [ 
    path('menu-items',views.menu_items),
    path('menu-items/<int:id>',views.single_item),
    path('category/<int:pk>',views.category_detail, name='category-detail')
]
```

## M2: Different types of renderers

### Introduction
Renderers are the core classes in DRF that display the API output in different formats like JSON and XML. You’ve already learned how to use the Browsable API renderer, JSON renderer, and a third-party renderer called XMLRenderer. In this reading, you are going to learn about a few other useful renderers that you can use in your API projects in DRF.

#### TemplateHTMLRenderer
Sometimes, even in an API project, it might be required to display HTML output. For example, if you generate an invoicing API, you need to display the transaction and order details in a nicely formatted way using HTML and CSS. In such cases, DRF’s TemplateHTMLRenderer can help. 

**Step 1**
Using the TemplateHTMLRenderer, you can pass the data to an HTML file and then display that data using Django’s native templating language called DTL, or Django Templating Language. 

To test this TemplateHTMLRenderer the menu items need to be displayed in an HTML file instead of JSON. To use this renderer, you first import it from the rest_framework.renderers module in the views.py file. You also need to import the renderer_classes decorator. 

```py
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
```

**Step 2**
The second step is to create a new function called menu in the views.py file. 
```py
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items.html')
```
Note how the serialized data is passed as context to the HTML template file named menu-items.html. You need to put this HTML file inside the templates directory in your Django app, so the path of this file is: LittleLemon/LittleLemonAPI/templates/menu-item.html

**Step 3**
The third step is to add the following templating code to this HTML file. This code block accepts the template data and displays them in a HTML table. 

```html
<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Menu Items</title>
</head>
<body>
    <table width="100%" style="text-align: left;">
        <tr>
            <th>Item</th> <!-- item column heading -->
            <th>Price</th> <!-- price column heading -->
            <th>Price After Tax</th> <!-- price after tax column heading -->
            <th>Stock</th> <!-- stock column heading -->
        </tr>
        {% for item in data %}
        <tr>
            <td>{{ item.title }}</td>
            <td>{{ item.price }}</td>
            <td>{{ item.price_after_tax }}</td>
            <td>{{ item.stock }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

It's possible that once you run the code, you may get an error such as TemplateDoesNotExist. This could happen if the settings don't find the correct directory for the templates and the Base directory needs to be set up. 

To fix this, go inside the settings.py file and make sure that the settings for the Templates are present. If they are not present, you can add code such as:

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Alternatively, if you see the code for the Templates and still get the error, try adding the code below:

```py
TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']
```

**Step 4**
The final step is to map the function to an API endpoint in the urls.py file so that it can be browsed as http://127.0.0.1:8000/api/menu.
```py
from django.urls import path 
from . import views 
urlpatterns = [ 
    path('menu-items',views.menu_items),
    path('menu-items/<int:id>',views.single_item)
    path('menu',views.menu),
]
```
Now the http://127.0.0.1:8000/api/menu API endpoint displays all the menu items in a nicely formatted HTML table.    

#### StaticHTMLRenderer
You can use the StaticHTMLRenderer if any of your API endpoints need to display some HTML content without using any DTL code inside an HTML file.  

**Step 1**
The first step is to import the StaticHTMLRenderer class and renderer_classes decorator like before. 
```py
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
```

**Step 2**
Then you need to create a new function called welcome in the views.py file. 

```py
@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)
```

**Step 3**
The final step is to map this endpoint to an API endpoint. This time, you want to display this message whenever someone visits the endpoint http://127.0.0.1:8000/api/welcome. To do this, you need to open the urls.py file and add the following line to the urlpatterns list: 
```py
path('welcome',views.welcome)
```
This greeting will now display if someone visits this endpoint. 

#### CSV renderer
CSV, or comma-separated values, is another popular format used by API developers. Unlike JSON or XML, every field in a database record is displayed separated by a comma and every record is on a new line. 

**Step 1**
DRF doesn’t come with a CSV renderer class by default. So the first step is to install a popular third-party package using pipenv. 
```bash
pipenv install djangorestframework-csv
```

**Step 2**
Import this renderer in the views.py file.
```py
from rest_framework_csv.renderers import CSVRenderer
```

**Step 3**
Add the renderer using the renderer_classes decorator to convert an API endpoint to display CSV instead of JSON. Add the following line of code in the menu-items function after the @api_view() decorator:
```py
@renderer_classes([CSVRenderer])
```
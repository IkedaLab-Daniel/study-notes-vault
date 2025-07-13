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
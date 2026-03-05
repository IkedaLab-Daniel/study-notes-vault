from django.http import HttpResponse

# Create your views here.
def home(request):
    html = """
    <div>
        <h1 style="color: red;">Hello</h1>
    </div>
"""
    return HttpResponse(html)
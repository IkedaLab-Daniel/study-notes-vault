from django.http import HttpResponse

# Create your views here.
def home(request):
    html = """
    <div>
        <h1 style="color: red;">Hello</h1>
    </div>
"""
    return HttpResponse(html)

def drinks(request, drink_name):

    drink = {
        "mocha": "type of coffee",
        "tea": "type of beverate",
        "lemonade": "type of refreshment"
    }
    if not drink_name in drink:
        drink[drink_name] = "probably delicious"

    return HttpResponse(f"<h1>Drink name: {drink_name} is a {drink[drink_name]}</h1>")
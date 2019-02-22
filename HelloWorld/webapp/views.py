from django.http import HttpResponse
import textwrap
# Create your views here.

def index(request):
    helloResponse = textwrap.dedent('''\
    <html>
    <head>
        <style>
        body {
            background-color: black;
            }
        h1 {
            color: blue;
            text-align: center;
            }
        </style>
        <title> Django Hello World </title>
    </head>
    <body>
        <h1> Hello World!</h1>
    </body>
    </html>
    ''')
    return HttpResponse(helloResponse)

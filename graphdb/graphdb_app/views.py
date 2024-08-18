from django.shortcuts import render

from django.shortcuts import render
from .models import GraphDB

def index(request):
    graphdb = GraphDB.objects.all()
    return render(request, 'index.html', {'graphdbs': graphdb})

def add_graphdb(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        blazegraph_url = request.POST['blazegraph_url']
        blazegraph_user = request.POST['blazegraph_user']
        blazegraph_password = request.POST['blazegraph_password']
        graphdb = GraphDB(name=name, description=description, blazegraph_url=blazegraph_url, blazegraph_user=blazegraph_user, blazegraph_password=blazegraph_password)
        graphdb.save()
        return render(request, 'index.html', {'graphdb': GraphDB.objects.all()})
    return render(request, 'add_graphdb.html')

def upload_ttl(request):
    if request.method == 'POST':
        ttl_file = request.FILES['ttl_file']
        # Upload TTL file to Blazegraph
        # ...
        return render(request, 'index.html', {'graphdb': GraphDB.objects.all()})
    return render(request, 'upload_ttl.html')

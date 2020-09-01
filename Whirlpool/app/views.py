from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
def index(request):
	return render(request, "index.html")

def main(request):
	if request.method == 'POST': #feeds us title, date
		new_item = Item(title=request.POST["title"], date=request.POST["date"])
		new_item.save()

	items = sorted(Item.objects.all())
	content = {
		'items': items
	}

	return render(request, "main.html", content)

def update(request, url_path):
	item = Item.objects.get(id=url_path)
	print(item)

	content = {"item": item}

	if request.method == 'POST':
		item.title = request.POST["title"]
		item.date = request.POST["date"]
		item.save()
		return redirect('/main')

	return render(request, "update.html", content)

@csrf_exempt
def delete(request, item_id):
	print("hello world")
	item = Item.objects.get(id=item_id)
	item.delete()
	return redirect('/main')

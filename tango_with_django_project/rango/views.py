from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
	"""
	Query the database for a list of all the categories currently stored
	Order the categories by no. likes in descending Order
	Retrieve the top 5
	Place the list in our context_dict
	"""
	category_list = Category.objects.order_by("-likes")[:5]
	page_list = Page.objects.order_by("-views")[:5]
	context_dict = {'categories' : category_list, 'pages': page_list}
	return render(request, 'rango/index.html', context_dict)

def category(request, category_name_slug):
	#Create a context dict
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name

		pages = Page.objects.filter(category = category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	return render(request, 'rango/category.html', context_dict)


def about(request):
	return HttpResponse("Rango says here is the about page.<br/> <a href='/rango/'> Index </a>")
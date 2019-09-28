from django.shortcuts import render
from .models import Reporter, Article


# Create your views here.
def index(request):
	# results are displayed with respect to class Article (from models)	
	filtered_Articles_john = Article.objects.filter(reporter__first_name="John")
	list_articles_john=list()
	for articles in filtered_Articles_john:
		list_articles_john.append(articles.headline)
	
	filtered_email_Sanpreet = Article.objects.filter(reporter__first_name="Sanpreet")
	list_article_sanpreet=list()
	for articles in filtered_email_Sanpreet:
		list_article_sanpreet.append(articles.headline)

	# results are displayed with respect to class Reporter (from models)
	filtered_name_using_article_j=Reporter.objects.filter(article__headline="another heading by John Smith") 
	list_name_j = list()
	for name in filtered_name_using_article_j:
		list_name_j.append(name.first_name + " " + name.last_name) 

# context is used because jinja template needs a context to be diplayed
# on the web page	
	context = {
		"articles_john": list_articles_john,
		"articles_sanpreet" : list_article_sanpreet,
		"list_name_j": list_name_j,
				}

	# print("show the dictionary please....", context)

	return render(request, 'filter_results.html', context)

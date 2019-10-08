from django.shortcuts import render
from .models import Reporter, Article

""" If you delete a reporter, his articles will be deleted (assuming that the ForeignKey was defined with django.db.models.ForeignKey.on_delete set to CASCADE, which is the default):"""

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

	all_records_reporter = Reporter.objects.all()
	""" fetch all the ids present in the table Reporter"""
	list_reporter_id = list()
	for reporter_id in all_records_reporter:
		list_reporter_id.append(reporter_id.id) 
	"""passing each_id to the another table as this is relational database"""
	for each_id in list_reporter_id:
		print(Article.objects.filter(reporter__pk=each_id))
	# count all the entries (Reportors) whose headline starts with 'This'
	# repeatation is allowed		
	print("All entries............")
	print(Reporter.objects.filter(article__headline__startswith='This').count())	

	# count only unique entries (Reporters whose headline starts with 'This')
	# Only Unique entries
	print()
	print("Only Unique entries............")
	print(Reporter.objects.filter(article__headline__startswith='This').distinct().count())
	
	# ordering a queryset in ascending order
	print()
	print("Ordering in ascending order......")
	print("Ordering Reporters by last_name.........")
	print(Reporter.objects.order_by('last_name'))

	# ordering a query set in descending oder
	# special thanks to https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
	print()
	print("Ordering in descending order using -")
	print("Ordering Reporters by last_name.........")
	print(Reporter.objects.order_by('-last_name'))

	# context is used because jinja template needs a context to be diplayed
	# on the web page	
	context = {
		"articles_john": list_articles_john,
		"articles_sanpreet" : list_article_sanpreet,
		"list_name_j": list_name_j,
				}

	# prin	t("show the dictionary please....", context)

	return render(request, 'filter_results.html', context)


from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs



# Create your views here.
def url_scrapper(url):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.9"
    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    response = session.get(url)
    results = {}
    try:
        soup = bs(response.text, 'html.parser')
        results['title'] = soup.find('title').text
        results['link_count'] = len(soup.findAll('a'))
    except:
        results = {}

    return results



def home_view(request):
    template_name = 'index.html'
    if request.method == "POST" and 'url' in request.POST:
        url = request.POST.get('url')
        results = url_scrapper(url)
        context = {'results': results}
    else:
        context={}
    return render(request, template_name, context)




    

        
        
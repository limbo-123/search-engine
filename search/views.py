from django.contrib.auth import admin
from django.http import response, request
from django.shortcuts import render
from selenium import webdriver
from search.models import submit, url
import time, os
from django.db.models import Q
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys

def home(request):
    return render(request, 'index.html')
def search(request):
    if request.method == 'GET':
        query = request.GET.get('url')
        if query is not None:
           lookup = Q(title__icontains = query) | Q(url__icontains = query) | Q(description__icontains = query) | Q(meta__icontains = query)
           result = submit.objects.filter(lookup)
           result_count = submit.objects.filter(lookup).count
           context = {
               'result': result,
               'result_count': result_count
           }
           return render(request, 'search.html', context)
        else:
           return render(request, 'index.html')  
def user_panel(request):
    if request.method=="POST":
        urls = url()
        web_url = request.POST.get('url')
        urls.url = web_url
        urls.save()
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        web_driver = webdriver.Chrome(executable_path=os.path.join("/usr/bin/chromedriver"),   chrome_options=chrome_options)
        web_driver.get(web_url)
        time.sleep(10)
        title_pre = web_driver.find_element_by_tag_name('title').get_attribute("innerText")
        urls.links = web_driver.find_elements_by_xpath("//*[@href]")
        body_pre = web_driver.find_element_by_tag_name('body')
        body_post = body_pre.text
        elems = web_driver.find_elements_by_tag_name('a')
        for elem in elems:
           href = elem.get_attribute('href')
        submit_web_data = submit()
        try:    
           meta_pre = web_driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content")
           submit_web_data.meta = meta_pre
        except Exception as e:
           print("Oops!", e.__class__, " Error occurred.")
        submit_web_data.url = web_url
        submit_web_data.description = body_post
        submit_web_data.title = title_pre
        submit_web_data.total_links = '6'
        submit_web_data.save()
        web_driver.close()
    return render(request, 'user_panel.html')



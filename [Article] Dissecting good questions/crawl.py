import beautifulSoup
import request

page = request.get('https://iamsteve.me/blog/entry/about-version-six')
print(page.html)
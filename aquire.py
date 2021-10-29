import urllib.request


html_lst = ['www.google.com', 'www.python.org', 'www.apple.com',
            'www.bing.com', 'www.yahoo.com', 'www.wikipedia.org',
            'www.washingtonpost.com', 'www.twitter.com', 'www.facebook.com', 'www.ebay.com']

for url in html_lst:
    html_res = urllib.request.urlopen(f'https://{url}/')
    html_content = html_res.read()
    file = open(f'serverfile/{url}.html', 'w', encoding='utf-8')
    file.write(html_content.decode())
    file.close()
# This work is licensed under the Creative Commons Attribution 4.0 International License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
# author : Morad Edwar
# license : Creative Commons
# version : 1.0
# email : me@morad-edwar.com
# status : Beta
import requests
from lxml import html
from urlparse import urljoin,urlparse
from datetime import datetime
# Edit the following lines
# Your website and don't forget http://
start_url = 'http://www.domain.com'
# Your Domain with www or not if you are not using it in the internal links
domain = 'www.domain.com'
# The sitemap path in your system
# Please note that the script writen for linux
# So if you're using windows use a different path
sitemap_path = '/tmp/sitemap.xml'
# The change frequency
frequency = 'Daily'
# The priority
priority = 'None'
# Ignore list to ignore links which you don't want to include it.
ignore = ['.jpg','.png','/user?id=','login','logout']

# Don't Edit anything bellow that line
# The visited links list to ignore them later
visted_links = []
# Open the file to write
sitemap_file = open(sitemap_path, "w")

def download(url):
    if not url in visted_links:
        visted_links.append(url)
        print "[" + str(datetime.now().time()) + "] Crawling : " + url
        sitemap_file.write('<url>\n')
        sitemap_file.write('<loc>'+url+'</loc>\n')
        sitemap_file.write('<changefreq>'+frequency+'</changefreq>\n')
        sitemap_file.write('<priority>'+priority+'</priority>\n')
        sitemap_file.write('</url>\n')
        request = requests.get(url, allow_redirects=False)
        content = html.fromstring(request.text)
        links = content.xpath('//a/@href')
        links = filter(links)
        for link in links:
            if not link in visted_links:
                for url in link:
                    download(url)

def filter(urls):
    links = []
    urls = map(lambda s: urljoin(start_url,s), urls)
    for url in urls:
        ignore_flag = False
        for word in ignore:
                if word in url:
                    ignore_flag = True
        if domain == urlparse(url).hostname and ignore_flag is False and not url in visted_links:
            links.extend([url])
    yield links

# The sitemap header
sitemap_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap_file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
# Start The script
download(start_url)
# Footer of the file
sitemap_file.write('</urlset>')
sitemap_file.close()
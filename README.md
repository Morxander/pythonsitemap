# SiteMap Generator
This is a free open source script licensed under the Creative Commons Attribution 4.0 International Licensender 
- author : Morad Edwar
- license : Creative Commons
- version : 1.0
- email : me@morad-edwar.com
- status : Beta

### Version
1.0

### Using

You just need to modify :

```sh
start_url = 'http://www.domain.com'
domain = 'www.domain.com'
sitemap_path = '/tmp/sitemap.xml'
frequency = 'Daily'
priority = 'None'
ignore = ['.jpg','.png','/user?id=','login','logout']
```
Then run it 
```sh
$ python sitemap.py
```
### Todo's

 - White list
 - Download delay




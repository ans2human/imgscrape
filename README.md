# Imgscrape

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)  [![Coverage Status](https://coveralls.io/repos/github/ans2human/imgscrape/badge.svg?branch=master)](https://coveralls.io/github/ans2human/imgscrape?branch=master)
    
Imgscrape is a [selenium](https://www.seleniumhq.org/) and [pillow](https://pypi.org/project/Pillow/) based image scraper.

 ### Supported Websites
  - **[Flipkart](https://www.flipkart.com/)**
  - **[Amazon](https://www.Amazon.in/)**

### Features!

  - Scrapes  image link
  - Convert image into thumbnail
  - Encode image into Base64 
  - Save image directly to folder  :  **In development**


Imgscrape is a [selenium](https://www.seleniumhq.org/) and [pillow](https://pypi.org/project/Pillow/) based image scraper. You just provide the product link or a list of the same and it will provide you the links in image or list of it based on your argument.


>The reason behind this idea is to scrape image links are unreachable by using [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Thus switching to selenium gets you the images you need.

### Installation & Usage

```sh
$ pip install imgscrape
```
- Imgscrape requires [chromedriver](http://chromedriver.chromium.org/downloads) to run. Download it.
- After downloading you'll need to provide the path of chromedriver to the constructer.

```e.g
from imgscrape import imgscrape

any_var = #path to driver      
var = imgscrape(producturl, path= any_var)
```
- you can feed a list of product urls and get the image links in a list.
```
from imgscrape import imgscrape

any_var = #path to driver
lst_var = ['link1', 'link2', 'link3']
var = imgscrape(*lst_var, path= any_var)
```


### Development

Want to contribute? Great!
Create a pull request and we'll see.

#### Support
- **linux**
- **windows**
- 
### Todos

 - Add support for MacOS
 - Add more supported websites

License
----

- MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)



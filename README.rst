Imgscrape
=========


.. image:: https://travis-ci.org/joemccann/dillinger.svg?branch=master
   :target: https://travis-ci.org/joemccann/dillinger
   :alt: Build Status
  
.. image:: https://coveralls.io/repos/github/ans2human/imgscrape/badge.svg?branch=master
   :target: https://coveralls.io/github/ans2human/imgscrape?branch=master
   :alt: Coverage Status


Imgscrape is a `selenium <https://www.seleniumhq.org/>`_ and `pillow <https://pypi.org/project/Pillow/>`_ based image scraper.

Supported Websites
^^^^^^^^^^^^^^^^^^


* `Flipkart <http://www.flipkart.com/>`_

* `Amazon <https://www.Amazon.in/>`_

Features!
^^^^^^^^^


* Scrapes  image link
* Convert image into thumbnail
* Encode image into Base64 
* Save image directly to folder  :  **In development**

Imgscrape is a `selenium <https://www.seleniumhq.org/>`_ and `pillow <https://pypi.org/project/Pillow/>`_ based image scraper. You just provide the product link or a list of the same and it will provide you the links in image or list of it based on your argument.

..

   The reason behind this idea is to scrape image links are unreachable by using `Beautifulsoup4 <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_. Thus switching to selenium gets you the images you need.


Installation & Usage
^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

   $ pip install imgscrape


* Imgscrape requires `chromedriver <http://chromedriver.chromium.org/downloads>`_ to run. Download it.
* After downloading you'll need to provide the path of chromedriver to the constructer.

.. code-block::

   from imgscrape import imgscrape

   any_var = #path to driver      
   var = imgscrape(producturl, path= any_var)


* you can feed a list of product urls and get the image links in a list.

.. code-block::

  from imgscrape import imgscrape

  any_var = #path to driver
  lst_var = ['link1', 'link2', 'link3']
  var = imgscrape(*lst_var, path= any_var)


Development
^^^^^^^^^^^

Want to contribute? Great!
Create a pull request and we'll see.

Support
~~~~~~~


* **linux**
* **windows**
* 
  ### Todos


  * Add support for MacOS
  * Add more supported websites

License
-------


* MIT

**Free Software, Absolutely**

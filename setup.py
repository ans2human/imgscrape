from distutils.core import setup
setup(
  name = 'imgscrape',        
  packages = ['imgscrape'],   
  version = '0.1',      
  license='MIT',        
  description = ' A piece of cake way to scrape product images from Amazon or flipkart',   
  author = 'Anshuman Anand Singh',                   
  author_email = 'ans2human@gmail.com',      
  url = 'https://github.com/ans2human/imgscrape',   
  long_description=open('README.rst').read(),
  download_url = 'https://github.com/ans2human/imgscrape/archive/v0.1.2.tar.gz',    
  keywords = ['FLIPKART', 'AMAZON', 'SCRAPING', 'SCRAPE', 'IMAGE', 'PRODUCTIMAGES'],   
  install_requires=[            
          'pillow',
          'selenium',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
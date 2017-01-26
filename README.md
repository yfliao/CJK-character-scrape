# Chinese Character Scraping Tool

\*\* Only Python versions 3.3+ are supported! Please ensure that you have the most recent Python 3.x.x installed before continuing. \*\*

This is a python CLI tool to be used to retrieve all Chinese characters from a webpage via data scraping and the BeautifulSoup4 module. 
Then using the returned and filtered text, alongside the definitions are outputted into a .csv file.
The corresponding character definitions are provided using CC-CEDICT, which you can find more about [here.](https://cc-cedict.org/wiki)

__NOTE:__ Please take caution as to the websites you are scraping your information from. Some sites may explicitly have restrictions in their
Terms of Use as to how the website's information can be used. In most cases, you should check the Terms of Use first and exclusively use this as
a personal tool.

## How to Install

There are several requisite modules that need to be installed before you can run this application:

  - httplib2 - A HTTP Client library.
  - BeautifulSoup4 - A library primarily centered around efficiently pulling data from HTML/XML files. 
  
```shell

# Install requisite files using pip. 

$ pip install beautifulsoup4
$ pip install httplib2

```

## How to Use

Please ensure you have the requisite files installed (specified above). From the command line you can run the app using the following format:

'''shell
  
  # The argument following main.py is mandatory.
  
  $ python main.py website_url [output_dir]
  
'''

The provided uri can be provided without a scheme with the default scheme falling back to *http://*. The second argument is optional and will fallback to a output folder located in the root directory of the application. If there are permissions difficulties, a further fallback to the home directory will occur. If the same situation occurs again the app will write a message to the console and exit. The value of the specified output directory can be relative or absolute, with a relative directory being based from the root directory.

An example of a CLI invocation could be:

'''shell
  $ python main.py https://example.org /documents/CJKScrape
'''

#### \*\*THIS CODE IS STILL VERY MUCH IN DEVELOPMENT AND NOT SUITABLE FOR PRODUCTION AS OF YET.\*\*

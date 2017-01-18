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
  
## TODO ##

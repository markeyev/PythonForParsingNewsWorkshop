# Python for parsing news workshop

What we will discuss?

[XML](https://en.wikipedia.org/wiki/XML), [RSS](https://en.wikipedia.org/wiki/RSS), 
[pypi](https://pypi.org/), [feedparser](https://feedparser.readthedocs.io/en/latest/), 
[API](https://en.wikipedia.org/wiki/API), [REST](https://en.wikipedia.org/wiki/Representational_state_transfer), 
[gRPC](https://grpc.io/), [CLI](https://en.wikipedia.org/wiki/Command-line_interface), 
[click](https://click.palletsprojects.com/).

In Python, everything is relatively simple. Whenever an idea comes into your mind, 
most likely someone already solved half of your problems and all you need is to 
find the result of their work.

Instead of "How?", you might want to ask first "What tools could be used to solve 
this problem?"

Example questions and easy answers:

1. How can I easily start testing my ideas in Python? 

   Answer: https://colab.research.google.com/

2. What package should I choose to solve my problem / test my new idea?

   Answer: https://pypi.org and https://python.libhunt.com/

3. I found the tool, but I don't know how to use it?
   
   Answer: really depends on what you like? 
   
   - You like watching YouTube videos?
   Please [search](https://www.youtube.com/results?search_query=feedparser+python)
   the library name on YouTube.
   - You like reading? Search library name on https://medium.com or 
     https://realpython.com/ or https://stackoverflow.com/.

4. Python packages are awesome! Can I create one?

   Answer: Yes! Please read Python official documentation on Packaging 
   https://packaging.python.org/tutorials/packaging-projects/, but if it is not 
   enough please read https://realpython.com/pypi-publish-python-package/.
   
## Examples

You can find code examples in the `examples` folder.

1. A small example of how to parse RSS feed with feedparser (you can use https://colab.research.google.com/ to run this code).
2. The same idea, but with feedparser_wrapper package to get sanitized content from posts (works in colab too).
3. An example of usage pymongo library for storing posts data in Mongo DB on your localhost (couldn't be used in colab).
4. The minimal example of REST API JSON response with flask.
5. An example of getting REST API JSON response with one of the most popular Python library - requests.

## Solution 

You can find the code of the solution in the `solution` folder. To run in please install
docker and docker-compose, and run terminal command `docker-compose run cli` 
from `solution` the folder.

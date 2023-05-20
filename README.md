# Assessment
 Python microservice that takes a URL of a static website as input and identifies unique words along with their frequency of occurrence, 
 returning the result in JSON format.
 To run this microservice, you'll need to install the required dependencies requests, beautifulsoup4, and flask.
 
 After installing the dependencies, you can start the microservice by running the Python script. 
 It will run on http://localhost:5000 by default.

You can send a POST request to http://localhost:5000/analyze with the URL of the static website in the request body. 
The microservice will extract the text from the web page, identify the unique words and their frequency, 
and return the result in JSON format.


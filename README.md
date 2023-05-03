This is a little **toy example** for running the Python web server Flask in a docker container on a linux host.

*Requirements:* Docker

*How to start:* `start_webservice.sh`

*Remarks*: Flask prints the url it listens on during start. Probably something like: http://172.17.0.2:5000. Open that url in your browser.

**If you don't want to use docker**

* Install python3-pip
* Install Flask using pip: `pip install flask`
* Start the webservice: python3 webservice.py

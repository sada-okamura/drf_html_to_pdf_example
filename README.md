# HTML to PDF example

## Goal

* Render HTML from Django Rest framework's serializer object
* Create PDF from the HTML
* Return PDF as HTTP response

## Technology used

* [Jinja2](http://jinja.pocoo.org/docs/2.10/)

    Template engine to generate HTML from serializer

* pdfkit

    Utility to use wkhtmltopdf from python


* [wkhtmltopdf](https://wkhtmltopdf.org/)

    command line tools to render HTML into PDF

## How to run this example?

Start the container
```bash
# from root directory of this example
# create docker image
docker build -t html2pdf:latest .


# run docker image with your local source directory mounted as volume
docker run --rm  -v $(pwd):/code -p 8000:8000 -n html2pdf html2pdf

# [first time only] create superuser
docker exec -it html2pdf python manage.py createsuperuser --email admin@example.com --username admin

# stop container (also remove container if --rm option is given with docker run command
doker stop html2pdf

```

Try accessing `http://127.0.0.1:8000/users/1/?pdf=1` from your browser.


## Todo

* Build `wkhtmltopdf` binary

    So far, I haven't been able to simply install wkhtmltopdf by `apk add wkhtmltopdf`.

    According to [madnight](https://github.com/madnight/docker-alpine-wkhtmltopdf/blob/master/Dockerfile), building wkhtmltopdf binary for alpine takes hours. Therefore a binary needs to be pre-build.

    Currently, a binary supplied by [madnight/docker-alpine-wkhtmltopdf](https://github.com/madnight/docker-alpine-wkhtmltopdf) is used.
    For production use, mainly for security reasons, we should be creating similar base image but using our own binary.


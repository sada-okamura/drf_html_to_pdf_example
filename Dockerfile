FROM madnight/docker-alpine-wkhtmltopdf as wkhtmltopdf

FROM python:alpine3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apk add --update --no-cache \
    libgcc libstdc++ libx11 glib libxrender libxext libintl \
    libcrypto1.0 libssl1.0 \
    ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-ubuntu-font-family

COPY --from=wkhtmltopdf /bin/wkhtmltopdf /bin/
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/

CMD ["/code/docker-entrypoint.sh"]

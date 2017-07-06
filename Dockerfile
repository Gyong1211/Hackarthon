FROM        ym4199/hackarthon_ubuntu
MAINTAINER  ym4199@gmail.com


COPY        . /srv/hackarthon
WORKDIR     /srv/hackarthon
RUN         /root/.pyenv/versions/hackarthon/bin/pip install -r .requirements/deploy.txt

COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/

COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

# collectstatic 실행
RUN         /root/.pyenv/versions/hackarthon/bin/python /srv/hackarthon/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput

CMD         supervisord -n




EXPOSE      80 8000
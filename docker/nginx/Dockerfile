FROM nginx:1.25.4-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./docker/nginx/nginx.conf /etc/nginx
COPY ./docker/nginx/proxy_params /etc/nginx/conf.d/

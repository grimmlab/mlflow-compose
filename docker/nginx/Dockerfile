FROM nginx:1.17.6

ARG USERNAME
ARG PASSWD
RUN apt-get update
RUN apt-get install -y apache2-utils
# Remove default Nginx config
RUN rm /etc/nginx/nginx.conf
# Copy the modified Nginx conf
COPY nginx.conf /etc/nginx
RUN htpasswd -bc /etc/nginx/.htpasswd $USERNAME $PASSWD
# Copy proxy config
COPY mlflow.conf /etc/nginx/sites-enabled/
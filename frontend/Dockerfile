FROM nginx:alpine

# Install OpenSSL
RUN apk update && \
    apk add --no-cache openssl

# Argument for SSL certificate CN
ARG NGINX_SSL_CN

# Generate self-signed SSL certificate
RUN mkdir -p /etc/ssl/private/ && mkdir -p /etc/ssl/certs/ && \
   openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
   -keyout /etc/ssl/private/nginx.key \
   -out /etc/ssl/certs/nginx.crt \
   -subj "/C=TR/ST=Kocaeli/L=Kocaeli/O=Ecole42/OU=transcendence/CN=${NGINX_SSL_CN}"

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy all frontend files into the web root
COPY index.html index.js /usr/share/nginx/html
COPY /public /usr/share/nginx/html/public
COPY /src /usr/share/nginx/html/src


# Set permissions
RUN chmod -R 755 /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]

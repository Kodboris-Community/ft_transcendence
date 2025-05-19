FROM nginx:alpine

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy frontend files into web root
COPY index.html index.js /usr/share/nginx/html/
COPY /public /usr/share/nginx/html/public/
COPY /src /usr/share/nginx/html/src/

# Set permissions
RUN chmod -R 755 /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]

# Use official NGINX image as base
FROM nginx:alpine

# Copy custom HTML into NGINX web directory
COPY html/ /usr/share/nginx/html

# Expose port (optional - handled by docker-compose too)
EXPOSE 80


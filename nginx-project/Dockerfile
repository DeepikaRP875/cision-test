# Use the official nginx base image from Docker Hub
FROM nginx:1.19-alpine

# Ensure nginx has the correct permissions
RUN mkdir -p /var/cache/nginx /var/run /var/log/nginx && \
    chown -R nginx:nginx /var/cache/nginx /var/run /var/log/nginx /etc/nginx
    
# Copy the HTML file to the Nginx HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Copy custom nginx configuration file 
COPY nginx.conf /etc/nginx/nginx.conf

# Switch to the non-root user
USER nginx

# Expose port 443 to the outside world
EXPOSE 443

# Start nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
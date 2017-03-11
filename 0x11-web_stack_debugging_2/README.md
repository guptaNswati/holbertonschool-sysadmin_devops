0x11-web_stack_debugging_2

0-run_nginx_as_nginx - Fix ubuntu container so that Nginx is running as
		     the nginx user with limited privileges, not as root.
		     Restrictions:
- nginx must be running as nginx user
- cannot use apt-get remove
- nginx must be listening on all active IPs on port 8080


1-fix_in_7_lines_or_less - Fix ubuntu container so that Nginx is running as
                     the nginx user with limited privileges, not as root.
		     Additional Requirements:
- script must be 7 lines long or less
- cannot use ; &&

# Commands used to change the root user
- service nginx status
- service nginx start
- service nginx status
- ps aux
- cat /etc/nginx/nginx.conf
- ls -al /etc/nginx/
- chmod 755 /etc/nginx/nginx.conf
- chown nginx /usr/share/nginx/
- su nginx -c nginx
- Tool: https://transfer.sh
- Ref: https://github.com/exratione/non-root-nginx/blob/master/nginx.conf

0x10-web_stack_debugging_1

0-nginx_likes_port_80 - contains bash script that debugs Nginx in an
		      ubuntu container's to find which port its listening
		      on and make it listen on 80

1-debugging_made_short - contains bash script that debugs Nginx in an
                      ubuntu container's to find which port its listening
                      on and make it listen on 80 with additional requirements
		      - script limit 5 lines
		      - service (init) must say that nginx is not running

# commands used to debug and fix
sudo service nginx status
sudo service nginx restart
cat /var/log/nginx/error.log
sudo netstat -pan
curl 0:8080
grep server /etc/nginx/sites-available/default
diff /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
cp /etc/nginx/sites-enabled/default ./default_backup
rm /etc/nginx/sites-enabled/default
cp /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
curl 0:80
sudo netstat -pan | grep 80
#!/usr/bin/python3
# web servers for the deployment of web_static
# install nginx if not installed

echo -e "\e[1;32m START\e[0m"
sudo apt update
sudo apt install -y nginx

echo -e "\e[1;32m Packages updated\e[0m"
echo

sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allow incoming NGINX HTTP connections\e[0m"
echo

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
echo -e "\e[1;32m directories created"
echo

echo "<html>
   <head><title>Testing My Domain</title></head>
   <body>
     <h1>Testing this page</h1>
   </body>
 </html>" > /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test string added\e[0m"
echo

if [ -d "/data/web_static/current" ];
then
	echo "path /data/webstatic/current exists"
	sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;32m prevent overwritting\e[0m"
echo

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-available/default'
echo -e "\e[1;32m Symbolic link created\e[0m"
echo

sudo service nginx restart
echo -e "\e[1;32m restart NGINX\e[0m"

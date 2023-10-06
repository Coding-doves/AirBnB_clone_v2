#!/usr/bin/env bash
# web servers for the deployment of web_static
# install nginx if not installed
if ! command -v nginx &> /dev/null
then
	sudo apt update
	sudo apt install -y nginx
fi

data="/data/"
web_static="$data/web_static/"
releases="$web_static/releases/"
shared="$web_static/shared/"
test_f="$releases/test/"
index="$test_f/index.html"
current="$web_static/current"
nginx="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static/ { alias $current/; }"

# create folders
if [ ! -d "$data" ]
then
	sudo mkdir -p $data
	sudo chown -R ubuntu:ubuntu $data
fi

if [ ! -d "$web_static" ]
then
	sudo mkdir -p $web_static
	sudo chown -R ubuntu:ubuntu $web_static
fi

if [ ! -d "$releases" ]
then
	sudo mkdir -p $releases
	sudo chown -R ubuntu:ubuntu $releases
fi

if [ ! -d "$shared" ]
then
	sudo mkdir -p $shared
	sudo chown -R ubuntu:ubuntu $shared
fi

if [ ! -d "$test_f" ]
then
	sudo mkdir -p $test_f
	sudo chown -R ubuntu:ubuntu $test_f
fi

# create fake html page
echo "<html>
   <head><title>Testing My Domain</title></head>
      <body>
        <h1>Testing this page</h1>
      </body>
 </html>" | sudo tee $index > /dev/null

# create symbolic link
sudo rm -rf $current

sudo ln -sf $test $current

sudo chown -R ubuntu:ubuntu /data/

sudo wget -q -O /etc/nginx/sites-available/default http://exampleconfig.com/static/raw/nginx/ubuntu20.04/etc/nginx/sites-available/default
config="/etc/nginx/sites-available/default"
echo 'Holberton School Hello World!' | sudo tee /var/www/html/index.html > /dev/null
sudo sed -i '/^}$/i \ \n\tlocation \/redirect_me {return 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;}' $config
sudo sed -i '/^}$/i \ \n\tlocation @404 {return 404 "Ceci n'\''est pas une page\\n";}' $config
sudo sed -i 's/=404/@404/g' $config
sudo sed -i "/^server {/a \ \tadd_header X-Served-By $HOSTNAME;" $config
sudo sed -i '/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config

sudo service nginx restart

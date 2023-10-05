#!/usr/bin/python3
# web servers for the deployment of web_static
# install nginx if not installed
sudo apt update
sudo apt install -y nginx

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
if [-L "$current"]
then
    sudo rm $current
fi

sudo ln -s $test $current

sudo sed -i "/^server {/a $nginx_alias" $nginx

sudo service nginx restart

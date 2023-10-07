#!/usr/bin/python3
'''
distributes an archive to your web servers, using the function do_deploy:

'''
import os
from datetime import datetime
from fabric.api import local, run, put, runs_once, env

env.hosts = ["54.144.147.44", "54.90.42.81"]
env.user = "ubuntu"

def do_deploy():
    """compressing the project"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    current_time = datetime.now()
    outpt = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            current_time.year, current_time.month,
            current_time.day, current_time.hour,
            current_time.minute, current_time.second
        )
    try:
        print("Packing web_static to {}".format(outpt))
        local("tar -cvzf {} web_static".format(outpt))
        archive_size = os.stat(outpt).st_size
        print("web_static packed: {} -> {} Bytes".format(outpt, archive_size))
    except Exception as e:
        print(e)
        outpt = None

    return outpt


def do_deploy(archive_path):
    """ comment """
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    folder_n = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_n)
    pas = False

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        pas = True
    except Exception as e:
        print("deploy2 failed")
        print(e)
        pas = False

    return pas

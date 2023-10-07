#!/usr/bin/python3
'''
 creates and distributes an archive to your web servers,
 using the function deploy
'''
import os
from datetime import datetime
from fabric.api import local, run, put, runs_once, env


env.hosts = ['54.144.147.44', '54.90.42.81']
env.user = "ubuntu"


@runs_once
def do_pack():
    """compressing the project"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    now_time = datetime.now()
    sta = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            now_time.year, now_time.month,
            now_time.day, now_time.hour,
            now_time.minute, now_time.second
            )
    try:
        print("Packing web_static to {}".format(sta))
        local("tar -cvzf {} web_static".format(sta))
        arch_size = os.stat(sta).st_size
        print("web_static packed: {} -> {} Bytes".format(sta, arch_size))
    except Exception:
        sta = None

    return sta


def do_deploy(arch_path):
    """ comment """
    if not os.path.exists(arch_path):
        return False

    file_name = os.path.basename(arch_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        put(arch_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")
        success = True
    except Exception as e:
        print("Deployment failed:", str(e))
        return False


def deploy():
    """
    comment
    """
    do_pack_deploy = do_pack()
    if not do_pack_deploy:
        return False
    dep = do_deploy(do_pack_deploy)
    return dep

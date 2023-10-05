#!/usr/bin/python3
'''
 creates and distributes an archive to your web servers,
 using the function deploy
'''
from fabric.api import env, put, run, local
from fabric.operations import local
from fabric.context_managers import cd
from datetime import datetime
import os
from os.path import exists


env.hosts = ['54.144.147.44', '54.90.42.81']


def do_pack():
    '''
    return the archive path if the archive has been correctly
    generated. Otherwise, it should return None
    '''
    try:
        local("mkdir -p versions")
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')

        local('tar -cvzf versions/{} web_static'.format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception as e:
        return None


def do_deploy(archive_path):
    '''commen'''
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        archive_f = os.path.basename(archive_path)
        release_fd = "/data/web_static/releases/{}".format(
                os.path.splitext(archive_f)[0])
        run('mkdir -p {}'.format(release_fd))
        run('tar -xzf /tmp/{} -C {}'.format(archive_f, release_fd))
        run('rm /tmp/{}'.format(archive_f))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_fd))
        return True
    except Exception as e:
        return False


def deploy():
    '''comment'''
    try:
        archive_path = do_pack()

        if archive_path is None:
            return False

        return do_deploy(archive_path)

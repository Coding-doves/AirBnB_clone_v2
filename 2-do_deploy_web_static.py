#!/usr/bin/python3
'''
distributes an archive to your web servers, using the function do_deploy:
'''
from fabric.api import env, put, run, local
import os
from os.path import exists
from datetime import datetime


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

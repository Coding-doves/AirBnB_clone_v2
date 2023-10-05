#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive
'''
from fabric.api import local
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

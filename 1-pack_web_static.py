#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive
'''
from fabric.decorators import runs_once
from fabric.api import local
from datetime import datetime


@runs_once
def do_pack():
    '''
    return the archive path if the archive has been correctly
    generated. Otherwiss, it should return None
    '''
    local("mkdir -p versions")
    timestamp = ("versions/web_static_{}.tgz".format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    loc = local('tar -cvzf versions/{} web_static'.format(timestamp))

    if loc.failed:
        return None
    print("Path", path)
    return timestamp

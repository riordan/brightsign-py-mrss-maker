from __future__ import print_function
import logging
import hashlib
import os
import mimetypes
from six.moves.urllib.parse import urljoin

import argparse


class MRImage:
    filePath = None
    link = None
    fileHash = None
    fileSize = None
    mimetype = None
    name = None
    displaytime = None


    def __init__(self, localpath, baseurl, displaytime=30):
        self.filePath = localpath
        self.fileSize = os.path.getsize(localpath)
        self.mimetype = mimetypes.MimeTypes().guess_type(localpath)[0]
        with open(localpath, 'rb') as f:
            self.fileHash = hashlib.sha1(f.read()).hexdigest()
        path, filename = os.path.split(localpath)
        self.name = filename
        pathcomponents = path.split('/')
        del pathcomponents[0]
        pathcomponents.append(filename)

        self.link = urljoin(baseurl, os.path.join(*pathcomponents))
        self.displaytime = displaytime

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


# parser = argparse.ArgumentParser(description='Create a BS Image')
# parser.add_argument("image", help="image location")
# args = parser.parse_args()
#
# i = MRImage(args.image, "http://sample.com/images")
# print(i)

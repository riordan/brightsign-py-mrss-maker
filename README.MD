mrss-maker
===========

Generates MRSS feed for a set of images

Generates MRSS for Brightsign, based on [Brightsign's Custom MRSS](http://support.brightsign.biz/hc/en-us/articles/218067267-Supported-Media-RSS-feeds).

Works for:
* video formats:
 * ts
 * mpg
 * vob
 * mov
 * mp4
* images
 * jpeg
 * bmp
 * png

Does not work for GIFs. Which is sad.

Each feed consists of:
* Own Filename (output location)
* MediaBaseURL: Root URL for all media (assumed to be entry level)
* Title
* Description
* Images
  * Image Things
  * Image Times


# Instructions
## Installation
```
virtualenv env #(or whichever location for virtualenvironment brightsign work)
source env/bin/activate
git clone <THIS REPOSITORY>
cd brightsign-py-mrss-maker
pip install -e .
```

## Usage
```
mrssMaker
usage: mrssMaker [-h] base_url feed_url media_folder

Create a Brightsign MRSS feed from a directory of images

positional arguments:
  base_url      Default location of MRSS assets when hosted (eg
                http://...01/content/media/)
  feed_url      Default location of MRSS feed assets when hosted (eg
                http://...01/content/feed.xml)
  media_folder  folder of media assets

optional arguments:
  -h, --help    show this help message and exit
```

# Background
This project is is derived from the [brown-brightsign-shows](https://github.com/riordan/brightsign-brown-shows) repository (defunct).

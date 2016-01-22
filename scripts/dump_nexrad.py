#From Lak's Blog http://eng.climate.com/2015/10/27/how-to-read-and-display-nexrad-on-aws-using-python/comment-page-1/#comment-2072

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy.ma as ma
import numpy as np
import pyart.graph
import tempfile
import pyart.io
import boto

s3conn = boto.connect_s3()
bucket = s3conn.get_bucket('noaa-nexrad-level2')
keys = bucket.get_all_keys(prefix = '2011/05/20/KVNX/')
print(keys[10].name.encode('utf-8'))
#so they are not all gzip files.. some tar files too

good_keys = []
datetimes = []
for key in keys:
    if 'gz' in key..name.encode('utf-8')


s3key = bucket.get_key('2015/05/15/KVWX/KVWX20150515_080737_V06.gz')
print)s3key)
localfile = tempfile.NamedTemporaryFile()
s3key.get_contents_to_filename(localfile.name)
radar = pyart.io.read_nexrad_archive(localfile.name)

keys = bucket.get_all_keys(prefix = '2011/05/20/KVNX/')


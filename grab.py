#!/usr/bin/env python
#import wget
#import datetime 
import urllib2
import cStringIO
import cv2
import time

url_base = 'http://www.seattle.gov/trafficcams/images/'
cam_list = [ \
    'Rainier_Henderson',
    'Rainier_Hudson',
    'MLK_Rainier', 
    'Rainier_MLK',
    ]
postfix = '.jpg'

start_time = time.strftime("%Y%m%d_%H%M%S") # str(datetime.datetime.now().time())
print 'start time', start_time

count = 10000000
while True:
    
    for ind, cam in enumerate(cam_list):
        url = url_base + cam + postfix
        try: 
            image_file = cStringIO.StringIO(urllib2.urlopen(url).read())
        except:
            continue
        cur_time = time.strftime("%Y%m%d_%H%M%S") # str(datetime.datetime.now().time())
            
        name = 'data/' + cam + '_' + start_time + "_" + str(count) + "_" + cur_time + postfix
        with open(name, 'w') as fh:
            fh.write(image_file.getvalue())
        #im = cv2.imread(image_file)
        #cv2.imshow(cam, image_file)

    count += 1
    # they don't update more than once a minute, or are otherwise preventing the same
    # requester from asking for them more often
    time.sleep(60.0)
    #cv2.waitKey(0)


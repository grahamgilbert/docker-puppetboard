#!/usr/bin/env python

import os

settings_file = '/srv/http/puppetboard/settings.py'
data = {}

data['PUPPETDB_HOST']       = os.getenv('PUPPETDB_HOST', 'localhost')
data['PUPPETDB_PORT']       = os.getenv('PUPPETDB_PORT', 8081)
data['PUPPETDB_SSL_VERIFY'] = os.getenv('PUPPETDB_SSL_VERIFY', True)
data['PUPPETDB_KEY']        = os.getenv('PUPPETDB_KEY', None)
data['PUPPETDB_CERT']       = os.getenv('PUPPETDB_CERT', None)
data['PUPPETDB_TIMEOUT']    = os.getenv('PUPPETDB_TIMEOUT', 20)
data['DEV_LISTEN_HOST']     = os.getenv('DEV_LISTEN_HOST', '127.0.0.1')
data['DEV_LISTEN_PORT']     = os.getenv('DEV_LISTEN_PORT', 5000)
data['UNRESPONSIVE_HOURS']  = os.getenv('UNRESPONSIVE_HOURS', 72)
data['ENABLE_QUERY']        = os.getenv('ENABLE_QUERY', True)
data['LOCALISE_TIMESTAMP']  = os.getenv('LOCALISE_TIMESTAMP', True)
data['LOGLEVEL']            = os.getenv('LOGLEVEL', 'info')
data['REPORTS_COUNT']       = os.getenv('REPORTS_COUNT', 10)
data['OFFLINE_MODE']        = os.getenv('OFFLINE_MODE', False)
data['GRAPH_FACTS']         = os.getenv('GRAPH_FACTS', 'architecture,domain,lsbcodename,lsbdistcodename,lsbdistid,lsbdistrelease,lsbmajdistrelease,netmask,osfamily,puppetversion,processorcount').split(',')


f = open(settings_file, 'w')

for key in data.keys():
    if isinstance(data[key], (int, bool, list, tuple)):
        f.write("{0} = {1}\n".format(key, data[key]))
    else:
        f.write("{0} = '{1}'\n".format(key, data[key]))

f.close()

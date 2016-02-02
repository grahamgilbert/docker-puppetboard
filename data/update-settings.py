#!/usr/bin/env python

import os

settings_file = '/srv/http/puppetboard/settings.py'
data = {}

data['PUPPETDB_HOST']       = os.getenv('PUPPETDB_HOST', 'localhost')
data['PUPPETDB_PORT']       = os.getenv('PUPPETDB_PORT', 8081)
try:
    if os.getenv('PUPPETDB_SSL_VERIFY', True).lower() == 'true':
        data['PUPPETDB_SSL_VERIFY'] = True
    elif:
        os.getenv('PUPPETDB_SSL_VERIFY', False).lower() == 'false':
            data['PUPPETDB_SSL_VERIFY'] = False
    else:
        data['PUPPETDB_SSL_VERIFY'] = os.getenv('PUPPETDB_SSL_VERIFY', False)
except:
    data['PUPPETDB_SSL_VERIFY'] = True

# Have we specified a key and a cert?
try:
    data['PUPPETDB_KEY'] = os.getenv('PUPPETDB_KEY')
except:
    pass

try:
    data['PUPPETDB_CERT'] = os.getenv('PUPPETDB_CERT')
except:
    pass
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

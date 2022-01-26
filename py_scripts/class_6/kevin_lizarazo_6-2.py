#!/usr/bin/env python

""" conf printer """ 

from config import conf

for element in conf:
    plugin_list = '  '
    domain = element['domain'] 
    plugins = element['plugins']
    database = element['database']
    host = element['database']['host']
    port = element['database']['port']
    for plugin in element['plugins']:
        plugin_list = plugin_list + plugin + '\n' + '  '
    print "domain: {} \ndb_host: {} \ndb_port: {} \nplugins: \n{}".format(
                                                                         domain, 
                                                                         host, 
                                                                         port, 
                                                                         plugin_list
                                                                         )
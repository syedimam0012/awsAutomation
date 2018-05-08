#!/usr/bin/env python

import boto3

rds = boto3.client('rds')

try:
    dbs = rds.describe_db_instances()

for db in dbs['DBInstances']:
    print ("%s@%s:%s %s") % (
          db['MasterUsername'],
          db['Endpoint']['Address'],
          db['Endpoint']['Port'],
          db['DBInstanceStatus']

except Exception as error:
    print error

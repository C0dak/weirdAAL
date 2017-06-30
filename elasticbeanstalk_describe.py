'''
This file is used to perform some ElasticBeanstalk actions
'''

import boto3
import botocore

import json
import urllib
import logging
import sys,os
import pprint

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.elasticbeanstalk import *

#insert AWS key, will figure out how to pull this in from a single file for all scripts

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

#describe_applications(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
#describe_application_versions(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
#describe_configuration_options(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
describe_environments(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
describe_events(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
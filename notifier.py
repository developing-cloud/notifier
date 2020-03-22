import os

import boto3

sns = boto3.client('sns')
""" :type : pyboto3.sns """

topic_arn = os.environ['SNS_ARN']


def lambda_handler(event, null):
    source = event['source']
    message = event['message']
    sns.publish(TopicArn=topic_arn, Subject=f'Message from {source}', Message=message)

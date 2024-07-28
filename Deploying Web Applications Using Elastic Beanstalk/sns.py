# import boto3

# from dotenv import load_dotenv
# import os
# import boto3

# # Load environment variables from .env file
# load_dotenv()

# # Get AWS credentials from environment variables
# aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
# aws_region = os.getenv('AWS_REGION')

# # Initialize SNS client
# sns_client = boto3.client('sns', region_name=aws_region,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)

# # Create SNS Topic
# def create_sns_topic(topic_name):
#     response = sns_client.create_topic(Name=topic_name)
#     return response['TopicArn']

# topic_arn = create_sns_topic('MyTopic')
# print(f'Topic ARN: {topic_arn}')

# # Subscribe to the Topic
# def subscribe_to_topic(topic_arn, protocol, endpoint):
#     response = sns_client.subscribe(
#         TopicArn=topic_arn,
#         Protocol=protocol,
#         Endpoint=endpoint
#     )
#     return response['SubscriptionArn']

# # Example for subscribing an email endpoint
# subscription_arn = subscribe_to_topic(topic_arn, 'email', 'itz.aman.av@gmail.com')
# print(f'Subscription ARN: {subscription_arn}')

# # Publish a Message to the Topic
# def publish_message(topic_arn, message, subject):
#     response = sns_client.publish(
#         TopicArn=topic_arn,
#         Message=message,
#         Subject=subject
#     )
#     return response

# response = publish_message(topic_arn, 'This is a test message', 'Test Subject')
# print(f'Message ID: {response["MessageId"]}')

import asyncio
from aiobotocore.session import get_session
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get AWS credentials from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')

async def main():
    session = get_session()
    async with session.create_client(
        'sns',
        region_name=aws_region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    ) as sns_client:

        # Create SNS Topic
        async def create_sns_topic(topic_name):
            response = await sns_client.create_topic(Name=topic_name)
            return response['TopicArn']

        topic_arn = await create_sns_topic('MyTopic')
        print(f'Topic ARN: {topic_arn}')

        # Subscribe to the Topic
        async def subscribe_to_topic(topic_arn, protocol, endpoint):
            response = await sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol=protocol,
                Endpoint=endpoint
            )
            return response['SubscriptionArn']

        # Example for subscribing an email endpoint
        subscription_arn = await subscribe_to_topic(topic_arn, 'email', '1ms19ei003@gmail.com')
        print(f'Subscription ARN: {subscription_arn}')

        # Publish a Message to the Topic
        async def publish_message(topic_arn, message, subject):
            response = await sns_client.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject=subject
            )
            return response

        response = await publish_message(topic_arn, 'This is a test message', 'Test Subject')
        print(f'Message ID: {response["MessageId"]}')

if __name__ == "__main__":
    asyncio.run(main())

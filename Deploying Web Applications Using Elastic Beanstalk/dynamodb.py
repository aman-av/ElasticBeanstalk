import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Get AWS credentials from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION')
username = 'abcd'
email = '1ms19ei003@gmail.com'
password = 'abcd1234'
table_name = 'MyTable'

# DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

# Function to create a table if it doesn't exist
def create_table():
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'Username',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Username',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print(f"Table '{table_name}' created successfully.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"Table '{table_name}' already exists.")
        else:
            print(f"Unexpected error: {e}")

# Function to add an item to the table
def add_item():
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
            'Username': username,
            'EmailID': email,
            'Password': password,
        }
    )
    print("Item added:", response)

def get_item_by_key(username):
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(Key={'Username': username})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response.get('Item')

# Main execution
if __name__ == "__main__":
    # create_table()
    # add_item()
    item=get_item_by_key(username)
    if item:
        print("Retrieved item:", item)
    else:
        print("Item not found.")

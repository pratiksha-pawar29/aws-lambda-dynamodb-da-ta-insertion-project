import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):

    # Generate unique user ID
    user_id = str(uuid.uuid4())

    # Get data from event
    name = event.get('name')
    email = event.get('email')

    # Insert into DynamoDB
    table.put_item(
        Item={
            'user_id': user_id,
            'name': name,
            'email': email
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'User created successfully',
            'user_id': user_id
        })
    }
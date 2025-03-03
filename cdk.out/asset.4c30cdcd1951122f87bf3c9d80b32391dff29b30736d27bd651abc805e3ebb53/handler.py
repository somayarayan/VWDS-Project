import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DataTable')

def lambda_handler(event, context):
    # Extract JSON data from the event
    data = json.loads(event['body'])
    
    # Example: Insert data into DynamoDB
    try:
        response = table.put_item(
            Item={
                'id': data['id'],
                'data': data['data']
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Data successfully saved to DynamoDB')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }


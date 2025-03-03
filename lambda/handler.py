import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VWDSStack-DataTable447BC44E-SSSUVNFD2L4C')  # Use the correct table name here

def lambda_handler(event, context):
    # Assuming event contains the data
    item = {
        'id': event['id'],
        'data': event['data']
    }

    # Try to put the item into the DynamoDB table
    try:
        response = table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps('Item successfully added to DynamoDB')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["YOUR_TABLE_NAME"])

def lambda_handler(event, context):
    connection_id = event["requestContext"]["connectionId"]

    # Store new connection in DynamoDB
    table.put_item(
        Item={
            "connectionId": connection_id
        }
    )

    print(f"New client connected: {connection_id}")

    return {"statusCode": 200}

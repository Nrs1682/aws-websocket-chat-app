import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["YOUR_TABLE_NAME"])

def lambda_handler(event, context):
    connection_id = event["requestContext"]["connectionId"]

    # Remove connection from DynamoDB
    table.delete_item(
        Key={"connectionId": connection_id}
    )

    print(f"Client disconnected: {connection_id}")

    return {"statusCode": 200}

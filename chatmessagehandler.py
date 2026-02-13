import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["YOUR_TABLE_NAME"])

def lambda_handler(event, context):

    body = json.loads(event["body"])
    username = body.get("username", "Anonymous")
    message = body.get("message", "")

    domain = event["requestContext"]["domainName"]
    stage = event["requestContext"]["stage"]

    apigw = boto3.client(
        "apigatewaymanagementapi",
        endpoint_url=f"https://{domain}/{stage}"
    )

    response = table.scan()
    connections = response.get("Items", [])

    for item in connections:
        conn_id = item["connectionId"]

        try:
            apigw.post_to_connection(
                Data=json.dumps({
                    "username": username,
                    "message": message
                }),
                ConnectionId=conn_id
            )
        except Exception as e:
            print(f"Failed to send to {conn_id}: {str(e)}")

    return {
        "statusCode": 200,
        "body": json.dumps({"status": "sent"})
    }

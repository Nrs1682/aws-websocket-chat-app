This project is a real-time serverless chat application built using WebSocket APIs on AWS. It enables multiple users to communicate instantly without refreshing the browser.

The backend is fully serverless and event-driven.

🛠 Tech Stack

Amazon Web Services

Amazon API Gateway (WebSocket API)

AWS Lambda

Amazon DynamoDB

Amazon CloudWatch

HTML, CSS, JavaScript

🔄 Architecture Workflow

Client connects to WebSocket endpoint

$connect route stores connection ID in DynamoDB

Messages sent via sendMessage route

Lambda broadcasts message to all active connections

$disconnect removes inactive users

✨ Features

Real-time two-way communication

Fully serverless backend

Event-driven architecture

Automatic connection lifecycle handling

CloudWatch logging for debugging

📷 Project Screenshots
Chat Interface

API Gateway WebSocket Routes

🎯 Key Learnings

WebSocket API configuration

Lambda route integration

DynamoDB connection management

IAM permission setup

Cloud debugging using CloudWatch
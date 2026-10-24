AWS Lambda DynamoDB Data Insertion
A serverless AWS project that demonstrates how to insert user data into Amazon DynamoDB using AWS Lambda, Python, and IAM least-privilege permissions.

Project Overview
This project demonstrates a serverless data insertion workflow using AWS Lambda and Amazon DynamoDB. The Lambda function receives user data through a test event and uses the DynamoDB PutItem operation to store the data in the users table.

IAM permissions are configured with the required PutItem action and restricted to the specific DynamoDB table using its ARN.

AWS Services Used
AWS Lambda
Amazon DynamoDB
AWS IAM
Technologies Used
Python 3.13
Boto3
JSON
AWS Management Console
Architecture
AWS_Lambda_DynamoDB_Architecture

Architecture Flow
Test Event → AWS Lambda → Amazon DynamoDB

IAM Role → Provides PutItem permission to Lambda

DynamoDB Configuration
Table Name: users
Partition Key: user_id
Data Type: String
Table Settings: Default
Lambda Configuration
Function Name: insert-dynamodb
Runtime: Python 3.13
Creation Method: Author from scratch
Operation: DynamoDB PutItem
IAM Permissions
The Lambda execution role is configured with an inline IAM policy containing:

Action: dynamodb:PutItem
Resource: Specific users DynamoDB table ARN
This follows the principle of least privilege by providing only the required access to the required DynamoDB resource.

Project Workflow
1.Created the users DynamoDB table.
2.Created the insert-dynamodb Lambda function.
3.0Configured the Python Lambda code.
4.Configured the Lambda execution role.
5.Added DynamoDB PutItem permission.
6.Restricted the permission to the specific table ARN.
7.Created a Lambda test event with user data.
8.Invoked the Lambda function using Save and test.
9.Verified the inserted data in the DynamoDB table.
* Key Features
-Serverless architecture
-DynamoDB data storage
-Python-based Lambda function
-IAM least-privilege access
-Table-level resource restriction
-Secure and scalable data insertion

Conclusion:This project demonstrates secure and serverless data insertion using AWS Lambda and DynamoDB, with IAM least-privilege permissions for controlled table access.

Author

Pratiksha Pawar 
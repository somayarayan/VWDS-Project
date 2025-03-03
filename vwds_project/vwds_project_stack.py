from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb
)
from constructs import Construct

class VWDSStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB Table (as defined before)
        table = dynamodb.Table(
            self, "DataTable",
            partition_key=dynamodb.Attribute(name="id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Lambda function to process data
        lambda_function = _lambda.Function(
            self, "DataHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset("lambda")  # Folder with handler.py
        )

        # Grant Lambda permission to write to DynamoDB
        table.grant_write_data(lambda_function)

        # API Gateway to expose the Lambda function
        api = apigateway.LambdaRestApi(
            self, "VWDSEndpoint",
            handler=lambda_function,
            proxy=False
        )

        items = api.root.add_resource("items")
        items.add_method("POST")  # POST method to accept JSON data

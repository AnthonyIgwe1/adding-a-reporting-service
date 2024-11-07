import json
import boto3

def lambda_handler(event, context):
    # The ARN for the inventory report state machine.
    state_machine_arn = 'arn:aws:states:us-west-2:363548493921:stateMachine:StateMachine-TxPMfZ1c0i2l'

    # Input used when the state machine starts execution.
    input_data = {
      "presigned_url_str": "Testing that my email message works"
    }

    # Creates a Step Functions client and starts the state machine execution.
    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )

    return {
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'statusCode': 200,
        'body': json.dumps({'executionArn': response['executionArn']})
    }

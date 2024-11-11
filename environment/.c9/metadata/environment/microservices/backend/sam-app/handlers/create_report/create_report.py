{"filter":false,"title":"create_report.py","tooltip":"/microservices/backend/sam-app/handlers/create_report/create_report.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["import json","import boto3","","def lambda_handler(event, context):","    # The ARN for the inventory report state machine.","    state_machine_arn = 'STATE_MACHINE_ARN'","","    # Input used when the state machine starts execution.","    input_data = {","      \"presigned_url_str\": \"Testing that my email message works\"","    }","","    # Creates a Step Functions client and starts the state machine execution.","    client = boto3.client('stepfunctions')","    response = client.start_execution(","        stateMachineArn=state_machine_arn,","        input=json.dumps(input_data)","    )","","    return {","        'headers': {","            'Access-Control-Allow-Headers': 'Content-Type',","            'Access-Control-Allow-Origin': '*',","            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'","        },","        'statusCode': 200,","        'body': json.dumps({'executionArn': response['executionArn']})","    }",""],"id":1}],[{"start":{"row":5,"column":25},"end":{"row":5,"column":42},"action":"remove","lines":["STATE_MACHINE_ARN"],"id":2},{"start":{"row":5,"column":25},"end":{"row":6,"column":12},"action":"insert","lines":["arn:aws:states:us-west-2:363548493921:stateMachine:StateMachine-            ","TxPMfZ1c0i2l"]}],[{"start":{"row":5,"column":101},"end":{"row":6,"column":0},"action":"remove","lines":["",""],"id":3},{"start":{"row":5,"column":100},"end":{"row":5,"column":101},"action":"remove","lines":[" "]},{"start":{"row":5,"column":96},"end":{"row":5,"column":100},"action":"remove","lines":["    "]},{"start":{"row":5,"column":92},"end":{"row":5,"column":96},"action":"remove","lines":["    "]}],[{"start":{"row":5,"column":91},"end":{"row":5,"column":92},"action":"remove","lines":[" "],"id":4},{"start":{"row":5,"column":90},"end":{"row":5,"column":91},"action":"remove","lines":[" "]},{"start":{"row":5,"column":89},"end":{"row":5,"column":90},"action":"remove","lines":[" "]}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":64},"action":"remove","lines":["\"presigned_url_str\": \"Testing that my email message works\""],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":6},"end":{"row":9,"column":6},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1731016468561,"hash":"7d3911c5fb832cc4e839bd77ed6234cb18018171"}
import json
import random
import boto3
import os

#dynamo client
dynamodb = boto3.client('dynamodb')
#tableName = 'flux3000-feature-requests'
tableName = os.environ['TABLE_NAME']

#sns client
sns = boto3.client('sns')
# get topic arn from environment variable
topicarn = os.environ['TOPIC_ARN']
#topicarn = 'arn:aws:sns:us-west-2:161615149547:FeatureRequests'

def get_named_parameter(event, name):
    return next(item for item in event['parameters'] if item['name'] == name)['value']

def get_named_property(event, name):
    return next(item for item in event['requestBody']['content']['application/json']['properties'] if item['name'] == name)['value']

def createUserRequest(event):
    print("calling method: create feature request")
    userStoryName = get_named_parameter(event, 'userStoryName')
    userStoryDescription = get_named_parameter(event, 'userStoryDescription') 
    acceptanceCriteria = get_named_parameter(event, 'acceptanceCriteria')
    Priority = get_named_parameter(event, 'Priority')
    Dependencies = get_named_parameter(event, 'Dependencies')
    Tasks = get_named_parameter(event, 'Tasks')
    TaskAssignee = get_named_parameter(event, 'TaskAssignee')
    print (event)
    
    # TODO: implement creating featureRequest
    userRequestId = str(random.randint(1, 99999))

    
    item = {
            'userRequestId': {"S": userRequestId},
            'userStoryName': {"S": userStoryName},
            'userStoryDescription': {"S": userStoryDescription},
            'acceptanceCriteria': {"S": acceptanceCriteria},
            'Priority': {"S": Priority},
            'Dependencies': {"S": Dependencies},
            'Tasks': {"S": Tasks},
            'TaskAssignee': {"S": TaskAssignee}
        }

    dynamodb.put_item(
        TableName=tableName,
        Item=item
        )
    
    response = sns.publish(
        TopicArn=topicarn,
        Message=f"your user story request {userStoryName} has been created and assigned to {TaskAssignee}",
        Subject="Feature Request Successfully Created"
    )
    
    print(response['MessageId']) 


    return {
        'body': f"Created request {userRequestId} in {tableName}"
    }

def updateUserRequest(event):
    print(event)
    
    # featureRequestID = str(get_named_parameter(event, 'featureRequestID'))
    # customerName = get_named_parameter(event, 'customerName')
    

    # # TODO: implement delete from dynamo here?
    # key = {
    #     'featureRequestID': {"S": featureRequestID},
    #     }

    # attribute_updates = {
    #     'customerName': {'Value': {'S': customerName}}
    # }

    # dynamodb.update_item(
    #     TableName=tableName,
    #     Key=key,
    #     AttributeUpdates=attribute_updates
    # )

    # response = sns.publish(
    #     TopicArn=topicarn,
    #     Message=f"your feature request {featureRequestID} has been updated by trevx@amazon.com",
    #     Subject="Feature Request Successfully Updated"
    # )
    
    response = sns.publish(
        TopicArn=topicarn,
        Message=f"Update function is successfully called",
        Subject="Function call successful"
    )

    print(response['MessageId']) 

    # Return a success message
    # return { 
    #     'body': f"Updated request {featureRequestID} in {tableName}"
    # }
    return { 
        'body': f"Update function is successfully called"
    }

def lambda_handler(event, context):

    result = ''
    response_code = 200
    action_group = event['actionGroup']
    api_path = event['apiPath']

    print("DEBUG: Lambda event ", str(event))
    print("DEBUG: Lambda context ", str(context))

    print ("lambda_handler == > api_path: ",api_path)
    
    if api_path == '/createUserRequest':
        result = createUserRequest(event)
    elif api_path == '/updateUserRequest':
        result = updateUserRequest(event)
    else:
        response_code = 404
        result = f"Unrecognized api path: {action_group}::{api_path}"

    response_body = {
        'application/json': {
            'body': json.dumps(result)
        }
    }
    
    print ("Event:", event)
    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        # 'httpMethod': event['HTTPMETHOD'], 
        'httpMethod': event['httpMethod'], 
        'httpStatusCode': response_code,
        'responseBody': response_body
    }

    api_response = {'messageVersion': '1.0', 'response': action_response}
        
    return api_response
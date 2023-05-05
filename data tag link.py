import boto3
import json
def lambda_handler(event, context):
    client = boto3.client('lakeformation')
    account_id = '012918428775'
    tag_data_access = {
					'role': 'arn:aws:iam::012918428775:role/SSFCMGOASIS_DEV_MCDM_LF_POC_DR_DEVELOPER',
                    'object_type' : 'table',
					'tag_expression': "'mcdm_test_tag1' = 'sales','mcdm_test_tag2' = 'iqvia'",
					'resource_action': 'SELECT'
    }
    data_tag_function(tag_data_access)
    def data_tag_function(tag_data_access):
        tag_expression = tag_data_access['tag_expression'].replace(' ','')
        format_expression = '['
        tag_expression_split = tag_expression.split(',')
        for i in range(len(tag_expression_split)) :
            format_expression = format_expression + "{'TagKey': " + tag_expression_split[i].split('=')[0] + ",'TagValues': ["\
                + tag_expression_split[i].split('=')[1] + "]},"
        format_expression = format_expression[:-1] + ']'
        format_expression = json.loads(format_expression.replace("'",'"'))
        response_tag_data_access=client.grant_permissions(    
                        CatalogId=account_id,
                        Principal={
                            'DataLakePrincipalIdentifier': tag_data_access['role']
                        },
                        Resource={
                            'LFTagPolicy': {                                 
                                'CatalogId': account_id,
                                'ResourceType': tag_data_access['object_type'],
                                'Expression': format_expression
                            }
                        },
                        Permissions=[
                            tag_data_access['resource_action']   
                        ]
                    )
    
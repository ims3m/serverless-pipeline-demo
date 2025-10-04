def lambda_handler(event, context):
    """
    AWS Lambda handler function for the serverless pipeline demo.
    
    Args:
        event: API Gateway event object
        context: Lambda context object
        
    Returns:
        dict: API Gateway response object
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
        },
        'body': '{"message": "App is running...", "status": "success"}'
    }
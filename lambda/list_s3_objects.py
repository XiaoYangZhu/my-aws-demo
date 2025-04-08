import boto3
import json

def lambda_handler(event, context):
    """
    Lambda function to list objects in an S3 bucket
    
    Parameters:
    event (dict): Event data passed to the function
    context (object): Runtime information
    
    Returns:
    dict: Response containing S3 objects or error message
    """
    try:
        # Get bucket name from environment variable or event
        bucket_name = event.get('bucket_name', None)
        
        if not bucket_name:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Bucket name not provided'})
            }
        
        # Initialize S3 client
        s3_client = boto3.client('s3')
        
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # Extract object keys
        objects = []
        if 'Contents' in response:
            for obj in response['Contents']:
                objects.append({
                    'key': obj['Key'],
                    'size': obj['Size'],
                    'last_modified': obj['LastModified'].isoformat()
                })
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'bucket': bucket_name,
                'objects': objects,
                'count': len(objects)
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

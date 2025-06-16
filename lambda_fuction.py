import boto3
import json
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
TABLE_NAME = os.environ['TABLE_NAME']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # Try to get the most likely ID field
    event_id = event.get('bookingId') or event.get('eventId') or event.get('id') or 'unknown'
    organizer_email = event.get('organizerEmail')
    checked_in = event.get('checkedIn', False)

    if not checked_in:
        message = f"The room booking{' with ID ' + event_id if event_id != 'unknown' else ''} was auto-reclaimed due to no check-in."

        # Reclaim room
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Room Booking Reclaimed"
        )

    # Log to DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            'eventId': event_id,
            'timestamp': datetime.utcnow().isoformat(),
            'checkedIn': checked_in,
            'reclaimed': not checked_in
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Processed booking status.')
    }

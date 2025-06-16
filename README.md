#AutoReclaim – Smart Meeting Room Management System
🕒 Automatically reclaims unoccupied meeting rooms using AWS Lambda, DynamoDB, EventBridge, and SNS.

🚀 Elevator Pitch
AutoReclaim ensures meeting rooms are used efficiently by detecting unconfirmed bookings and automatically freeing them up for others. Perfect for busy workplaces with limited room availability!

🧠 Inspiration
Many organizations struggle with inefficient room usage, where rooms are booked but remain unused due to missed check-ins. We wanted to create a smart and automated way to reclaim such rooms, reducing waste and improving productivity. That’s how AutoReclaim was born — a serverless, event-driven solution that works silently in the background.

🛠️ Tech Stack
Category	Technology Used
Languages	Python
Cloud	AWS Lambda, EventBridge, IAM
Database	Amazon DynamoDB
Messaging	Amazon SNS
API Gateway	AWS API Gateway
CI/CD	GitHub

🏗️ Architecture


Workflow Overview:

A booking event (with eventId, organizerEmail, and checkedIn status) is sent to the backend via API Gateway.

AWS Lambda processes the event:

If not checked in, triggers Amazon SNS to notify the user.

Logs the event in DynamoDB.

AWS EventBridge Scheduler runs every 5 minutes to check for bookings needing reclaiming.

SNS sends email alerts for auto-reclaimed rooms.

Everything is serverless and cost-effective.

🧪 How AWS Lambda Is Used
AWS Lambda is the core compute service for this project. It handles:

Processing booking events (check-in status).

Reclaiming rooms by determining if a check-in happened.

Sending notifications via SNS.

Logging all operations into DynamoDB.

📅 How the Schedule Works
AWS EventBridge Scheduler runs every 5 minutes to trigger the Lambda function. It simulates a background check for bookings and ensures unused rooms are flagged and reclaimed in real-time.

🗄️ Data Model (DynamoDB)
Each booking is stored with the following schema:

{
  "eventId": "uuid-1234",
  "timestamp": "2025-06-16T09:25:00Z",
  "checkedIn": false,
  "reclaimed": true
}
🔐 IAM Roles
Custom IAM roles are used to:

Allow Lambda to access DynamoDB and publish to SNS.

Allow EventBridge to invoke the Lambda function on schedule.

🎥 Demo Video
📺 Watch Demo on Vimeo

💡 What We Learned
Efficient serverless design with AWS Lambda and EventBridge

Event-driven architecture patterns

Integrating DynamoDB, SNS, and Lambda seamlessly

Writing IAM policies and setting environment variables securely

🧗 Challenges Faced
Handling schedule-based automation using EventBridge

Debugging SNS email delivery formatting

Dynamically linking check-in logic with booking events

🧰 How to Run This Project
Deploy the Lambda function using AWS Console or SAM CLI.

Set up DynamoDB and SNS topic.

Attach the appropriate IAM role with necessary permissions.

Create an EventBridge Scheduler rule (cron every 5 mins).

Connect API Gateway if needed for booking events.
📂 Project Structure
├── lambda_function.py       # Main Lambda logic
├── template.yaml            # (If using SAM)
├── README.md                # Project documentation
└── architecture.png         # System architecture image


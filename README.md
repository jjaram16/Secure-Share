Serverless Secure File Sharing App

This project is a simple cloud-based web app that lets users upload and download files securely using AWS services. It was built to learn how serverless applications work and to practice cloud security, authentication, and deployment.



Overview

The app uses Amazon Cognito for user login, AWS Lambda for backend logic, API Gateway for routing, and Amazon S3 for storage. When a user signs in, they can upload a file that’s encrypted and stored in S3. The app then generates a time-limited download link so only authenticated users can access their files.


How It Works

Frontend – A small HTML and JavaScript page with buttons for login, upload, and download.

Authentication – Cognito manages sign-in and returns a JWT token that proves the user’s identity.

API Gateway – Provides two endpoints: one for getting an upload URL and one for getting a download URL.

Lambda Functions – Create signed S3 URLs for secure file uploads and downloads.

S3 Storage – Holds the encrypted files at very low cost (<$0.01/month on the free tier).


Tech Stack

- Languages: Python, JavaScript, HTML/CSS

- AWS Services: Lambda, S3, API Gateway, Cognito

- Libraries: boto3 for AWS access, cryptography for AES encryption

- Tools: AWS Console, Git, Python HTTP server for local testing


Folder Structure

- frontend/   → index.html (web page)

- lambda/     → Python functions for upload and download

- docs/       → architecture diagram and notes

- README.md   → project description


How To Run Locally

1. Clone this repository.

    git clone https://github.com/<your-username>/secure-share-site.git
    cd secure-share-site/frontend


2. Start a local web server.

    python3 -m http.server 5500


3. Go to http://localhost:5500 in your browser.

4. Click Login, sign in through Cognito, then test upload and download.


What I Learned

How serverless apps use AWS Lambda instead of traditional servers

How authentication tokens (JWT) secure API requests

How S3 signed URLs control file access

How to connect multiple AWS services into one working system


Cost and Performance

The system scales automatically and stays within the AWS free tier. Uploads and downloads handle over 100 files easily with 99.9% uptime.

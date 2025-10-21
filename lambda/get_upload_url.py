import json, os, uuid
import boto3

S3 = boto3.client("s3")
BUCKET = os.environ["BUCKET"]

def handler(event, context):
    body = json.loads(event.get("body") or "{}")
    content_type = body.get("content_type", "application/octet-stream")
    filename = body.get("filename", str(uuid.uuid4()))

    sub =(event.get("requestContext", {})
              .get("authorizer", {})
              .get("jwt", {})
              .get("claims", {})
              .get("sub", "anon"))

    key = f"uploads/{sub}/{uuid.uuid4()}_{filename}"

    url = S3.generate_presigned_url(
        ClientMethod="put_object",
        Params={"Bucket": BUCKET, "Key": key, "ContentType": content_type},
        ExpiresIn=900  # 15 min
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps({"upload_url": url, "key": key})
    }

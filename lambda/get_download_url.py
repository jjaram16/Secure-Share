import json, os, boto3

S3 = boto3.client("s3")
BUCKET = os.environ["BUCKET"]

def handler(event, context):
    qs = event.get("queryStringParameters") or {}
    key = qs.get("key")
    if not key:
        return {"statusCode": 400, "body": "missing key"}

    url = S3.generate_presigned_url(
        ClientMethod="get_object",
        Params={"Bucket": BUCKET, "Key": key},
        ExpiresIn=900
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
        "body": json.dumps({"download_url": url})
    }

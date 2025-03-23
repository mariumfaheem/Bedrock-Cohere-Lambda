import boto3
import json
import os

from dotenv import load_dotenv
load_dotenv()

bedrock=boto3.client(service_name="bedrock-runtime",
                     region_name="us-east-1",
                     aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                     aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                    aws_session_token=os.environ['AWS_SESSION_TOKEN'])

prompt_data="""
Act as a Shakespeare and write a poem on Genertaive AI
"""


payload={
    "prompt": prompt_data ,
    "max_tokens":512,
    "temperature":0.5,
    "p":1,
    "k":0
}
body=json.dumps(payload)


model_id="cohere.command-text-v14"
accept = "application/json"
contentType = "application/json"

response=bedrock.invoke_model(
 modelId = model_id,
 contentType= contentType,
 accept = accept,
 body = body
)
response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generations'][0]['text']
print(repsonse_text)


import sys, os, base64, datetime, hashlib, hmac 
import subprocess, re
import datetime
import time
import json

api_key = '0000000000' #enter Rev API Key Here
job_id = None

try:
    output = 'curl -X POST "https://api.rev.ai/revspeech/v1beta/jobs" -H "Authorization: Bearer ' + api_key + '" -H "Content-Type: application/json" -d "{' + r'\"' + 'media_url' + r'\"' + ':' + r'\"' + 'https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3' + r'\"' + ',' + r'\"' + 'metadata' + r'\"' + ':' + r'\"' + 'This is a sample submit jobs option' + r'\"' + '}"'
    res = subprocess.check_output(output, shell=True).decode('utf-8')
    res_data = json.loads(res)
    job_id = res_data['id']

except subprocess.CalledProcessError as e:
    print("Error Encountered :(")


try:
    res_data = {'current_value': 'in_progress'}
    while len(str(res_data))<300:
        time.sleep(1)
        output = 'curl -X GET "https://api.rev.ai/revspeech/v1beta/jobs/'+ job_id +'/transcript" -H "Authorization: Bearer ' + api_key + '" -H "Accept: application/vnd.rev.transcript.v1.0+json"'
        res = subprocess.check_output(output, shell=True).decode('utf-8')
        res_data = json.loads(res)
        print(res_data)
    print(res_data)

except subprocess.CalledProcessError as e:
    print("Error Encountered :(")

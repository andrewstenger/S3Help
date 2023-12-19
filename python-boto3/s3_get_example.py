import os
import boto3
import pandas as pd


bucket_name = 'bucket_name'
prefix      = 'path/to/data/'

# iterate through all objects in a bucket in the provided prefix, download the objects locally using the same directory-structure
for obj_summary in s3.Bucket(bucket_name).objects.filter(Prefix=prefix):
  key = obj_summary.key
  #local_filename = os.path.basename(key)
  local_filename = key
  s3.meta.client.download_file(bucket_name, key, local_filename)

# iterate the local files, do something with them
local_path = prefix
for root, dirs, files in os.walk(local_path):
  for filename in files:
    filepath = os.path.join(root, filename)
    # run process...

# you can pull CSVs directly off S3 with Pandas, using the complete S3 URI for the object as the path (URI is in the form "s3://<bucket>/<key>")
key = 'path/to/spreadsheet.csv'
df = pd.read_csv(f's3://{bucket_name}/{key}')

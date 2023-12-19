#!/usr/bin/env bash

BUCKET="bucket_name"
PREFIX="path/to/data/"

LOCAL_DIR="path/to/local/dir/"

# s3 sync is the most efficient/fastest way to download S3 data locally
# this command will "sync" the contents of the prefix in the bucket to the local directory
# you should always run this with the `--dryrun` argument to see what the command will do, before rerunning it without it
aws s3 sync s3://${BUCKET}/${PREFIX} ${LOCAL_DIR} --dryrun
aws s3 sync s3://${BUCKET}/${PREFIX} ${LOCAL_DIR}

# it works in both directions too, you can also upload with it, just change the order of the data-sources
aws s3 sync ${LOCAL_DIR} s3://${BUCKET}/${PREFIX} --dryrun

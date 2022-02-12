#!/bin/sh

bucket="aistemos-mark-day"
prefix="airflow/dags"
localpath="/tmp/dags"

while true
do
  aws s3 sync s3://"$bucket"/"$prefix"/ "$localpath/"
  echo "run" >> /tmp/run.tmp
  sleep 360
done

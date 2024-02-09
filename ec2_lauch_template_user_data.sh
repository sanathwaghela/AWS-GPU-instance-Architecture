#!/bin/bash
aws s3 cp s3://<bucket_url>/ec2_instance_bash_script.sh /home/ubuntu/ 
aws s3 cp s3://<bucket_url>/<file_name>.yml /etc/filebeat/filebeat.yml  ## filebeat config file 
sudo systemctl restart filebeat

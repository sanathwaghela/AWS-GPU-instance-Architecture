#!/bin/bash
for i in `aws autoscaling describe-auto-scaling-groups --auto-scaling-group-name asg-name | grep -i instanceid | awk '{ print $2}' | cut -d',' -f1| sed -e 's/"//g'`
do
instanceIp=`aws ec2 describe-instances --instance-ids $i | grep -i PrivateIpAddress | awk '{ print $2 }' | head -1 | cut -d"," -f1 | cut -d'"' -f2`
echo "Instance found: " $instanceIp
scp -i "<ssh_key_name>.pem" -o StrictHostKeyChecking=no ./<zip_filename>.zip ubuntu@$instanceIp:/home/ubuntu/
ssh -i "<ssh_key_name>.pem" -o StrictHostKeyChecking=no ubuntu@$instanceIp 'sudo bash ec2_instance_bash_script.sh'
echo "Script Updated on this node!"
done;

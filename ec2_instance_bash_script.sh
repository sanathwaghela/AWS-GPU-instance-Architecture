#!/bin/bash
## runs on remote ec2 instance
instance_type=`curl http://169.254.169.254/latest/meta-data/instance-type`
echo $instance_type
instance_type_without_quotes=$(echo $instance_type | sed 's/"//g')
echo $instance_type_without_quotes
case $instance_type_without_quotes in
"g4dn.xlarge")
unzip -o /home/ubuntu/<zip_filename> -d /home/ubuntu/<folder_name> && unzip -o /home/ubuntu/<zip_filename> -d /home/ubuntu/<folder_name>1
systemctl start <service_name> && systemctl start <service_name>1
echo "Deployed on g4dn.xlarge."
;;
"g4dn.2xlarge")
unzip -o /home/ubuntu/<zip_filename>  -d /home/ubuntu/<folder_name> && unzip -o /home/ubuntu/<zip_filename> -d /home/ubuntu/<folder_name>1 && unzip -o /home/ubuntu/<zip_filename> -d /home/ubuntu/<folder_name>2
systemctl start <service_name> && systemctl start <service_name>1 && systemctl start <service_name>2
echo "Deployed on g4dn.2xlarge."
;;
*)
echo "No valid Instance Found."
;;
esac

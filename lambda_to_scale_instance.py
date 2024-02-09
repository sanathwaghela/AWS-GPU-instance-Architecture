import boto3

## This lambda python script run every 15 min triggered by eventbridge
## it scales instance up and down based on sqs message present in queue

sqs = boto3.client('sqs', region_name='<aws_region>')
autoscaling = boto3.client('autoscaling', region_name='<aws_region>')

def lambda_handler(event, context):
    response_sqs1 = sqs.get_queue_attributes(QueueUrl='https://<sqs_url>', AttributeNames=['ApproximateNumberOfMessages'])
    count_sqs1 = response_sqs1['Attributes']['ApproximateNumberOfMessages']
    
    count_sqs = int(count_sqs1)
    print ("sqs message count = ", count_sqs)
    
    response_asg = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=['<ASG_NAME>'])
    desiredCount_asg = response_asg['AutoScalingGroups'][0]['DesiredCapacity']
    maxSize_asg = response_asg['AutoScalingGroups'][0]['MaxSize']
    print ("ASG desired instance count = ", desiredCount_asg)
    print ("ASG Maximum instance count = ", maxSize_asg)

    
    if count_sqs <= 4 :
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=0)
        print(response_desiredCount_asg)
        print ("ASG Scaled to 0")

    if count_sqs >= 5 and count_sqs < 200 : 
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=1)
        print(response_desiredCount_asg)
        print(f"Message in generate transcript : {count_sqs}")
        print("ASG Scaled to 1")

    if count_sqs >= 200 and count_sqs < 500 : 
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=2)
        print(response_desiredCount_asg)
        print(f"Message in generate transcript : {count_sqs}")
        print("ASG Scaled to 2")
        
    if count_sqs >= 500 and count_sqs < 1000 : 
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=3)
        print(response_desiredCount_asg)
        print(f"Message in generate transcript : {count_sqs}")
        print("ASG Scaled to 3")
    
    if count_sqs >= 1000 and count_sqs < 2000 : 
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=4)
        print(response_desiredCount_asg)
        print(f"Message in generate transcript : {count_sqs}")
        print("ASG Scaled to 4")
        
    if count_sqs >= 2000 and count_sqs < 3000 : 
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=5)
        print(response_desiredCount_asg)
        print(f"Message in generate transcript : {count_sqs}")
        print("ASG Scaled to 5")
        
    if count_sqs >= 3000 : 
        response_desiredCount_asg = autoscaling.update_auto_scaling_group(AutoScalingGroupName='<ASG_NAME>', DesiredCapacity=6)
        print(response_desiredCount_asg)
        print(f"Message in generate transcript : {count_sqs}")
        print("ASG Scaled to 6")

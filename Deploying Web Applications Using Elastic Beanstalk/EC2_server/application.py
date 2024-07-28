from flask import Flask, render_template, request
import boto3
from boto3.dynamodb.conditions import Key, Attr
application = Flask(__name__)

region = 'us-east-1'
accessKeyId = 'AKIA24JJ3WJ3IQAIS6GU'
secretAccessKey = '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'

#DynamoDB resource
dynamodb = boto3.resource('dynamodb',region_name=region,aws_access_key_id=accessKeyId,
         aws_secret_access_key=secretAccessKey)
table = dynamodb.Table('MyTable')

#SNS client
sns = boto3.client('sns',region_name=region,aws_access_key_id=accessKeyId,
         aws_secret_access_key=secretAccessKey)

#SNS topic ARN
sns_topic_ARN = 'arn:aws:sns:us-east-1:747948978806:MyTopic'

@application.route('/')
@application.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		response = table.scan(FilterExpression=(Attr('Username').eq(username) & Attr('Password').eq(password)))
		if response['Count'] != 0:
			sns_response = sns.publish(TopicArn=sns_topic_ARN, Message='You have logged in', Subject='Elastic Beanstalk Notification')            
			msg = 'Logged in successfully !'
			return render_template('home.html')
		else:
			msg = 'Incorrect username / password !'
			
	return render_template('login.html', msg = msg)

if __name__ == '__main__':
    application.run()
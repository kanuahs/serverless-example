# Serverless python example

A simple serverless service that deploys a AWS lambda function with 3 environment variables and exposes an api to retrieve them. Written in python.

## Dependancies
- [Install node](https://nodejs.org/en)
- [Install aws cli and configure credentials]( https://aws.amazon.com/cli/)
- Install serverless (global)

```npm install -g serverless```

## Setup
- clone git repository

`git clone <url>`
- login to serverless (if you want to use the dashboard)

`serverless login`
- change the following part in serverless.yml to the app, tennant in your account

```
app: myapp
tenant: kanuahs
```

## Development
- Put logic in handler.py and infrastructure details in serverless.yml
- Test locally

`serverless invoke local -f hello`

- deploy to aws

`serverless deploy #entire stack`

`serverless deploy -f hello #deploy function "hello"`

```
$serverless deploy

Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (2.53 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: env-test-lambda
stage: dev
region: <aws-region>
stack: env-test-lambda-dev
api keys:
  mykey: <x-api-key>
endpoints:
  GET - https://XXXXXXX.execute-api.REGION.amazonaws.com/dev/user/env
functions:
  hello: env-test-lambda-dev-hello
Serverless: Removing old service artifacts from S3...
Serverless: Publishing service to Serverless Platform...
Serverless: Successfully published your service on the Serverless Platform
Serverless: Service URL:  https://dashboard.serverless.com/tenants/TENANT_NAME/applications/APP_NAME/services/env-test-lambda
```

- Invoke the function using serverless

`serverless invoke -f hello`

- Invoke the function using curl

```
$curl https://XXXXXXX.execute-api.REGION.amazonaws.com/dev/user/env
{"message":"Forbidden"}

curl https://XXXXXXX.execute-api.REGION.amazonaws.com/dev/user/env --header "x-api-key":"<x-api-key>"
{
  "Username": "kanuahs",
  "Password": "totallysecurepassword",
  "Service": "Lambda"
}
```

- get cloudwatch logs

`serverless logs -f hello`

- delete the stack

`serverless remove`
```
$serverless remove
Serverless: Removing usage plan association...
Serverless: Getting all objects in S3 bucket...
Serverless: Removing objects in S3 bucket...
Serverless: Removing Stack...
Serverless: Checking Stack removal progress...
..................
Serverless: Stack removal finished...
Serverless: Successfully archived your service on the Serverless Platform
```

### Creating a service from a template
- Generates boilerplate code for specifed provider and language in the current directory

`serverless create -t <PROVIDER>-<LANGUAGE+/BUILDTOOL>`

```
serverless create -t hello-world

serverless create -t aws-nodejs
serverless create -t aws-python
serverless create -t aws-python3
serverless create -t aws-java-maven
serverless create -t aws-java-gradle
```

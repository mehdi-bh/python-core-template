# python-core

## 1. Activate virtual-env
- `source virtual-env/bin/activate`
- `pip install -r requirements.txt`

## 2. Run API in local
`python app.py`

## 3. Deploy on AWS
- API Gateway
- Lambda functions

1. Update the serverless.yml file, it is currently deploying an API Gateway and one lambda function for each route.
2. Run `serverless deploy`

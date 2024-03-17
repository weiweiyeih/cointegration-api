# Deploy FastAPI on AWS Lambda | In 9 MINUTES

https://www.youtube.com/watch?v=7-CvGFJNE_o&t=12

## Terminal

```
pip install fastapi uvicorn mangum
pip freeze > requirements.txt
pip list --format=freeze > requirements.txt # conda env
# Only need:
    fastapi==0.99.1
    mangum==0.17.0

1. pip3 install -t dependencies -r requirements.txt
# Install all dependencies in "dependencies" directory

2. (cd dependencies; zip ../aws_lambda_artifact.zip -r .)
3. zip aws_lambda_artifact.zip -u main.py

```

## `main.py`

```
handler = Mangum(app)
```

## AWS Lanmbda

1. Create a function -> Advanced settings

   - [x] Enable function URL

   - [x] Auth type: NONE

2. Upload from: `.zip file`

   `aws_lambda_artifact.zip`

3. Runtime settings -> Edit -> Handler

   `main.handler`

# Deploy FastAPI on AWS Lambda ⚡ Serverless hosting!

https://www.youtube.com/watch?v=RGIM4JfsSk0

## Deploying FastAPI to AWS Lambda

We'll need to modify the API so that it has a Lambda handler. Use Mangum:

```
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
```

We'll also need to install the dependencies into a local directory so we can zip it up.

```
# Install all dependencies in "lib" directory
# gitignore: lib
pip install -t lib -r requirements.txt
```

We now need to zip it up.

```
# gitignore: *.zip
(cd lib; zip ../lambda_function.zip -r .)
```

Now add our FastAPI file and the JSON file.

```
zip lambda_function.zip -u main.py
zip lambda_function.zip -u books.json
```

## AWS Lanmbda

1. Create a function -> default

2. Upload from: `.zip file`

3. Test

   1. Test event -> create new event -> Template: `apigateway-aws-proxy`

   2. Modify `path`: 4, 16, 117 & `httpMethod`: 5, 119

4. Configuration -> Function URL -> create

   - [x] Auth type: NONE

   - [x] Configure cross-origin resource sharing (CORS)

# Working with Environment Variables in AWS Lambda Function | Encrypt and Decrypt using KMS | LAB

https://youtu.be/-pEe75tExd0?t=245

1. Configuration -> Environment variables -> Create

2. Code

```
import os

my_secret_key = os.environ.get("MY_SECRET_KEY)
```

# Troubleshooting

https://stackoverflow.com/questions/76650856/no-module-named-pydantic-core-pydantic-core-in-aws-lambda-though-library-is-i

```
FastAPI==0.99.0
```

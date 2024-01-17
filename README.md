# ldParamSDK
Use LaunchDarkly's Python SDK to get flag value as part of an API. 

## Setup
1. Run 'pip install -r requirements.txt 
2. Run 'fask run'

## Curl example:
curl -X POST -H "Content-Type: application/json" -d '<key-for-user>' "http://127.0.0.1:5000//api/v1/flags?sdk=<server-side-key>"

## TODO:
- [ ] Add example of AllFlags(). Parse response.
- [ ] build context from request body JSON
// const axios = require('axios')
// const url = 'http://checkip.amazonaws.com/';
let response;

/**
 *
 * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
 * @param {Object} event - API Gateway Lambda Proxy Input Format
 *
 * Context doc: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html
 * @param {Object} context
 *
 * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
 * @returns {Object} object - API Gateway Lambda Proxy Output Format
 *
 */
exports.lambdaHandler = async (event, context) => {
  try {
    console.debug('checking');
    console.debug({ event });
    let auth = 'Deny';

    let c = event.AuthorizationToken;
    if (c === 'abc123') {
      auth = 'Allow';
    } else {
      auth = 'Deny';
    }

    response = {
      principalId: c,
      policyDocument: {
        Version: '2012-10-17',
        Statement: [
          {
            Action: 'execute-api:Invoke',
            Resource: [
              'arn:aws:execute-api:us-east-2:975633666349:1nbwmtkx97/*/POST/image',
            ],
            Effect: auth,
          },
        ],
      },
    };
  } catch (err) {
    console.log(err);
    return err;
  }

  return response;
};

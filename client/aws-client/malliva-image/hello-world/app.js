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

const AWS = require('aws-sdk');
const fs = require('fs');
const ACCESS_KEY_ID = 'xxxxxx';
const SECRET_ACCESS_KEY = 'xxxx';
AWS.config.update({ region: process.env.AWS_REGION });

const s3 = new AWS.S3({
  accessKeyId: ACCESS_KEY_ID,
  secretAccessKey: SECRET_ACCESS_KEY,
});
const URL_EXPIRATION_SECONDS = 300;
const UploadBucket = 'malliva-img-temp';

// Main Lambda entry point
exports.lambdaHandler = async (event) => {
  return await getUploadURL(event);
};

const getUploadURL = async function (event) {
  console.error({ event });
  //const data = JSON.parse(event);
  const key = event.key;
  const body = event.body;

  const bufBody = new Buffer.from(body, 'base64');

  // const bufBody = new Buffer.from(
  //   body.replace(/^data:image\/\w+;base64,/, ''),
  //   'base64'
  // );

  var params = {
    Bucket: UploadBucket,
    Key: key,
    Body: bufBody,
    ContentEncoding: 'base64',
    ContentType: 'image/jpeg',
    ACL: 'public-read',
  };

  return (response = await s3
    .putObject(params, function (err, data) {
      let res;
      if (err) {
        res = { error: err, event: event };
        console.log(err, err.stack);
      } else {
        res = {
          statusCode: 200,
          body: JSON.stringify(data),
        };
      }
      return res;
    })
    .promise());
};

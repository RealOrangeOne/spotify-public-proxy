import {
  APIGatewayProxyEvent,
  APIGatewayProxyCallback
  // @ts-ignore
} from '@types/aws-lambda'


exports.handler = (
  event: APIGatewayProxyEvent,
  context: any,
  callback: APIGatewayProxyCallback
) => {
  callback(null, {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json'
    },
    body: "{}"
  });
}

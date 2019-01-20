import {
  APIGatewayProxyEvent,
  APIGatewayProxyCallback
  // @ts-ignore
} from '@types/aws-lambda';

import request from 'request-promise-native';

const CLIENT_ID = process.env.SPOTIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SPOTIFY_CLIENT_SECRET;

const CLIENT_ID_ACCESS_TOKEN = Buffer.from(`${CLIENT_ID}:${CLIENT_SECRET}`).toString("base64");

async function getAccessToken() {
  const data = await request.post("https://accounts.spotify.com/api/token", {
    form: {
      grant_type: "client_credentials"
    },
    headers: {
      "Authorization": `Basic ${CLIENT_ID_ACCESS_TOKEN}`,
    }
  });

  return JSON.parse(data).access_token;
}

exports.handler = async (
  event: APIGatewayProxyEvent,
  context: any
) => {
  const access_token = await getAccessToken();
  return {
    statusCode: 200,
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      access_token
    })
  };
}

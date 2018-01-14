# Spotify Public Proxy

[![CircleCI](https://circleci.com/gh/RealOrangeOne/spotify-public-proxy.svg?style=svg)](https://circleci.com/gh/RealOrangeOne/spotify-public-proxy)

Proxy for reading publicly-accessible data from Spotify, without distributing tokens.

## Supported APIs
Due to the nature of the APIs, only `GET` calls are supported.

## How it works
On an incoming request, we request an access token from spotify, and append it to the request, before sending it on to spotifys standard API.
 
## Usage
### Host it yourself
So I don't have to handle hosting application costs of this, you will need to host an instance of this yourselves.

### Create a spotify application to get required tokens
Create an application at https://developer.spotify.com/my-applications/, and create a client ID and secret
### Setup tokens
```bash
export SPOTIFY_CLIENT_ID="..."
export SPOTIFY_CLIENT_SECRET="..."
```
### Start the server
    
    python3 ./src/app.py

### Send a request
Simply change the `https://api.spotify.com` with your instance URL. eg `https://your.spotify.proxy.com/v1/users/{user_id}/playlists/{playlist_id}`

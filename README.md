# Spotify Public Proxy

[![CircleCI](https://circleci.com/gh/RealOrangeOne/spotify-public-proxy.svg?style=svg)](https://circleci.com/gh/RealOrangeOne/spotify-public-proxy)

Proxy for reading publicly-accessible data from Spotify, without distributing tokens.

## Supported APIs
- Querying playlist data

## How it works
On an incoming request, the required calls to the `spotipy` module are called, and returned to the client. As the `spotipy` module handles authentication, the client doesn't need to send them.

## Differences from Spotify
As an MVP, this is incompatible with Spotify's API. Future updates will enable this to work as a simple proxy through.

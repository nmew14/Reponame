# DRM Uploader Bot

A simple Telegram bot to upload `.txt` files securely. Built with Pyrogram and Docker, and deployable on Render.

## Features
- Accepts `.txt` file uploads from a specific Telegram user.
- Environment variable-based secrets for secure deployment.
- Lightweight and Dockerized.

## Deployment (Render)
1. Clone or upload this repo.
2. Set the following environment variables on Render:
   - `BOT_TOKEN`
   - `API_ID`
   - `API_HASH`
   - `USER_ID`
3. Use the Dockerfile for deployment.

## Local Run
```bash
docker build -t drm-uploader .
docker run --env-file .env drm-uploader
```

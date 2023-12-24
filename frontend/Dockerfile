# syntax=docker/dockerfile:1

FROM node:20-alpine3.18 AS stage
WORKDIR /app/

# Add and install requirements
COPY ./package.json /app/package.json
RUN npm install

# Add .env variables
COPY ./.docker.env /app/.env

# Add project files
COPY ./public /app/public
COPY ./index.html /app/index.html
COPY ./package-lock.json /app/package-lock.json
COPY ./vite.config.js /app/vite.config.js
COPY ./src /app/src

# Build app (index.html and ../index-@@@.js, ../index-@@@.css) files
RUN npm run build


FROM nginx:stable

# Install nano
RUN apt-get -y update \
    && apt-get -y install nano

# Add app dist and nginx config files
COPY --from=stage /app/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["nginx-debug", "-g", "daemon off;"]

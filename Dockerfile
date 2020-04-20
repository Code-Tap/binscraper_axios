FROM node:12.16.2-alpine3.11 AS build

RUN apk add --update --no-cache \
    python3 \
    make \
    g++\
    yarn && \
    pip3 install --upgrade pip setuptools

WORKDIR /src
COPY ./package* ./

RUN yarn install --frozen-lockfile && \
    pip3 install scrollphat fourletterphat

COPY . .

CMD ["yarn","run","all"]
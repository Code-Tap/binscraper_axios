FROM arm32v6/node:12-alpine

RUN apk add --update --no-cache \
    python3 &&\
    pip3 install --upgrade pip \
    setuptools \
    smbus \
    scrollphat \
    fourletterphat

WORKDIR /src
COPY . .
RUN yarn install --frozen-lockfile
CMD ["yarn","run","all"]
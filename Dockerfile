FROM arm32v6/node:12-alpine

RUN apk add --update --no-cache \
    python3 \
    py3-smbus &&\
    pip3 install --upgrade pip \
    setuptools \
    smbus2 \
    scrollphat \
    fourletterphat

WORKDIR /src
COPY . .
RUN yarn install --frozen-lockfile
CMD ["yarn","run","all"]
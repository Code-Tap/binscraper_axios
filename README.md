# binscraper_axios
Node and Python Scripts to scrape and display visual bin collection day notification Walsall City Council and current date

Before you do anything you will need to create a .env file with the following info

```bash
ID=112233445566 
DURATION='?weeks=2'
```
you can obtain the relevent ID from this page (https://www.walsall.gov.uk/Waste/bincollections) by entering a valid postcode.
on the next page you simply need to open your dev tools and pull the refrence number for the required address.


Run Maunally:
Install dependencies with 

```bash
yarn install
```
run with 
```bash
yarn run all
```

Build the docker container:
```bash
docker build -t bintool .
```
```bash
docker run -d --privileged --restart=always bintool
```

The ```--privileged``` flag is required to allow the docker container to access the GPIO Pins of the raspberry pi.





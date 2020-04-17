# binscraper_axios
Node Script to scrape bin collection types and dates for Walsall City Council

Install dependencies with 

```bash
yarn install
```
run with 
```bash
node index.js
```

You will need to create an env file with the following info

```bash
ID=112233445566 
DURATION='?weeks=2'
```

you can obtain the relevent ID from this page (https://www.walsall.gov.uk/Waste/bincollections) by entering a valid postcode.
on the next page you simply need to open your dev tools and pull the refrence number for the required address.

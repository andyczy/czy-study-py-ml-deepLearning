# Scrapy 

a Module that scrape a business page on YP and return business name and phone

## Example

```js
var scrape = require('./scrape.js');
 var url = 'http://www.yellowpages.com/west-monroe-la/mip/armstrong-cricket-farm-5032804?lid=5032804'

 scrape(url, function(err, data) {
   if (err) {
     console.error(err);
   }

//   console.log(data);  => { name: 'Armstrong Cricket Farm', phone: '(318)387-6000' }
// });
```

## Methods

### var scrape = require('scrape');

```js
scrape(url, cb);
```

Get business name and phone of a given `url`. `cb` is a callback.

`cb(err, data)` fires with the scraped information.

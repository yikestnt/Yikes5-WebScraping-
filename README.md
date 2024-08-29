# Background of this research

Before getting into scraping, I need to determine which website I am going to scrape from. Earlier on I discovered that I had to do some experimentation on HOW to scrape, because there are different ways and they don't all work the same on different websites/brands.

Ranking of Jewelry Brands:
1. Van Cleef and Arpels 1906 ; 505.7M USD
    - https://www.vancleefarpels.com/us/en/the-maison/timeline/origins.html#:~:text=Born%20in%20the%20wake%20of,debut%20of%20a%20bejeweled%20destiny.
    - https://www.zoominfo.com/c/van-cleef--arpels/170328141
2. Cartier 1847 ; 6.2B
    - https://www.cartier.com/en-sk/maison/the-story/story-and-heritage
    - https://www.zippia.com/cartier-careers-18270/revenue/#
3. CatbirdNYC 2004 ; 60.2M USD
    - https://www.brooklynnavyyard.org/tenants/catbird/
    - https://growjo.com/company/Catbird_NYC#google_vignette
4. Laurie Fleming Jewelry approx. 2014
    - https://www.appmybizaccount.gov.on.ca/onbis/businessnames/viewInstance/view.pub?id=185e6c856f92f2744af3ee5b87a9ed2f11e4b9fc2c846b7587cb497c8c3736b9&_timestamp=4631642856566348
    
**Table 1: Jewelry brands and what methods can be used to scrape from them**

|Company|Basic Request| Selenium| Proxy| Web Scraping Service|
|:-----:|:-----------:|:-------:|:----:|:-------------------:|
|CatbirdNYC| No          | Yes       | x    | x              |
|Cartier| No          | x       | x    | x                   |
|Van Cleef and Arpels| No          | Yes       | x    | x                   |
|Laurie Fleming | Yes          | x       | x    | x              |
    
In terms of VCA versus Cartier ranking, VCA is known as more of an upscale brand for jewelry than Cartier because it is pricier and handmade.

# Intended Audience and Audience Background

Anyone is welcome to read through my "research"! It's for fun and for anyone who shares my interest (or even if they don't)! It's not extremely technical or thorough, to be clear, since I did some basic research and I did not cite sources for the most part. 

If any reader's would like to use this code, they need some technical background and basic coding ability. This code and task does not go into deeper topics like memory allocation, but knowledge on coding, scraping, website security, html, javascript, and more, will make it easier to understand (not that what I'm doing is terribly difficult). 

# Research Process

Before delving into the code, here is the outline of this notebook. To preface, I haven't scraped websites before besides using Reddit API years ago, so I don't have much knowledge or experience in these regards.

Check a websites robots.txt file before/during this process to have a better idea of what websites do or do not allow.

I am testing/trying to scrape from mainly Van Cleef and Arpels. I started with the basic requests library, and realized that didn't work on all jewelry websites, probably to prevent scraping from bots or scalpers. 

Based on the table above, in Table 1, you can see that the basic request only works on Laurie Fleming Jewelry's website and CatbirdNYC's website. It does not work on Van Cleef and Arpels, nor Cartier. I think the reason why is because higher end luxury companies have more resources for extra features like preventative measures on their websites, and these companies in particular have more incentive to protect against resellers/scalpers since their items are in hot demand and are worth a lot. 

When I couldn't scrape from VCA, I used Selenium. 

Selenium capabilities:
-  can interact with web pages the same way a real user would, including dynamically generated content from JavaScript
- allows you to perform actions on web elements such as clicking buttons, filling out forms, or scrolling
- can handle client-side validations, pop-ups, alerts, and cookies in real-time, replicating a user's session more accurately

The last point, was what I noticed was causing issues in the regular requests. My header information, particularly the cookies, was not correct or perhaps had session specific data that while executing it with the regular requests, caused issues and I could not retrieve the HTML data.

# How You Can Use This Code

My logic flow:

1. Get the website/page that has "out of stock" for the item you want
2. Add the link into the selenium code portion
3. Add email alerts (?) for restock notifications
4. Add your code with your specifications to a shell script to execute continuously 

I added code at the bottom that could be used to email yourself an alert when an item comes. I also added the simple shell script code that you would put this python code into.

# Questions

1. Can I cause issues by submitting a bunch of requests? Does that give me information on rate limits?
2. Can I get in trouble and/or banned for scraping?
3. What kind of capabilites are scraping APIs offering? Are they used by bots and scalpers? How useful is it for the tasks?

# Conclusion and Future Work

I learned that Selenium is an absolute must for scraping. I also don't know how these companies deal with bots, and I would not want them to block my IP, so I would also implement proxies to rotate my IPs. If I were to perform these searches on a larger scale, for example for multiple people wanting this information or on multiple items, I would look into using an API, both for the learning experience and for the convenience. I would also use a Google Chrome driver instead of a Safari driver, because it would be easier for the email notification portion. The reason why I didn't is because downgrading Google Chrome is difficult, and I didn't know how to downgrade it to match the driver (the latest version was newer than the newest driver).

If I continued this project, I would like to create a website for ease of use, that one could input some basic information and then sign up for alerts on restocks. That would require me to at a minimum:
- Pay for a scraping API service
- Create a website
- Implement a backend database for emails of users



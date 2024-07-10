Project Overview
This project involves scraping economic indicators from a specified website, cleaning the data, and storing it into CSV files. Initially, I encountered several challenges that required a change in approach.

Initial Approach
My first approach was to scrape the data in an unreadable format from the website and then attempt to clean it. However, this method proved to be very difficult and time-consuming.

Second Approach
Next, I scraped the data into two lists: one for the indicators and one for the values, with the intention of pairing them during the cleaning process. Unfortunately, I discovered that the indicators did not match consistently for each country, resulting in incorrect values being inserted into the CSV files.

Final Approach
I have decided to start the project anew with a different strategy. This time, I will pair the values with their corresponding indicators as I scrape the data, and insert 'None' for any missing values. This should ensure that the data is accurate and properly formatted.

the modified project will be in another repo and as soon ihave finished i will link it in here
this is the link of the version two of the project : https://github.com/baselnabil/economic_scrapingv2-

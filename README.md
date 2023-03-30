# CSC468-WCU CloudLab Project: SourceScan
## Group 8

The project runs through the use of Docker compose.
* Prestep: Clone in Group-8 github using the URL link
* Step 1: Go into /cloud-468/Group-8/worker
* Step 2: Run command "docker build -t test ." 
* Step 3: run command "docker run test"
* Step 4: Without errors, go into group 8 directory and run "docker compose up"
* Step 5: The program should deploy, with both running containers. Visit the Web address.
***
## Collaborators: 
* [Jason Kost](https://www.linkedin.com/in/jason-kost-587299224/)
* [Andrew Roche](https://www.linkedin.com/in/andrew-roche1/)
* [David Desjardins](https://www.linkedin.com/in/ddesj/)
* [Adesayo Ade-Oyetayo](https://www.linkedin.com/in/adesayo-ade-oyetayo/)

## Description: 
As we move into 2022, news stories are no longer confined to mainstream news sources. With the vast amount of information available on the internet, breaking news often surfaces on online message boards like Reddit, long before it reaches mainstream network news channels. However, given the sheer volume of news available from multiple sources on the internet, gathering relevant information can be a daunting task for individuals.

To streamline this process, we propose a software solution consisting of three components:

* API Reddit Scraper: Developed in Python language, this component takes a list of predetermined 'news source' subreddits, such as r/news, r/globalnews, and r/politics, and uses keywords provided by the user to gather all pertinent information surrounding the provided topic. The scraper's aim is to filter out irrelevant posts and provide only relevant submissions from each news-based subreddit.

* Redis Database: This database is designed around the concept of key terms inputted by the client and holds the gathered information after it is filtered. The database is called after the use of the scraper and is needed for the WebUI’s query in order to return the results to the user.

* Flask User Interface (WebUI): The WebUI component provides users with an easy-to-use interface, enabling them to filter information and display only relevant submissions. The WebUI queries the database after the scraper is deployed, returning submissions to the user that they can then view the details of.


The three-piece program aims to provide users with relevant news stories while saving them time and streamlining the news-searching process. By creating a program that can identify and filter useful information based on submitted key terms, immediately returning the resulting information into a database, and displaying that information in the database to the user, Redditors can ensure that they receive relevant news updates and avoid potentially misleading or fake news sources.

***
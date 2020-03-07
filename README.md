# Data Engineering Exercises

Below are some software development exercices. Note that we will use them to evaluate : 
1. Your knowledge and ability to use / learn scripting languages and technologies;
2. Your design / architecture / coding skills, and;
3. Your coding *best practices* (Commenting, Naming, Clean Code, DRY, TDD, etc...)
4. Your creativity.

## To Do 
1. Follow the instructions below while maintaining a presentable (clean) project. 
2. Over the next interview, we will ask that you present a demo of your work (environment set up, tools used, architecture, pipelines & APIs developped, scripts, etc...).
Use any presentation form you deem necessary (ppt, pdf, schema, drawings, code snippets, etc.) in addition to the live demo.

## Remember 
1. Ensure you apply best scripting/development practices.
2. Make assumptions where necessary.
3. The best of works goes unnoticed if not well explained - You only have 30-40min to present your work, focus on the important pieces.
4. Be creative.

**Good Luck!**
<br></br>
<br></br>


# Exercise 1 : Data Ingestion / RSS
1. Design and implement a pipeline to ingest the RSS feeds listed below and retrieve at a minimum the following info about the ingested articles when possible :
    - Timestamp
    - Author
    - Title
    - Link to the article
    - Tags (Categories, subcategories, etc...)
    - Descriptive text
2. Send the ingested data to an independent service described in *Exercise 2*

List of RSS feeds : 
- CBC Top Stories : https://rss.cbc.ca/lineup/topstories.xml
- CBC Montreal Regional News : http://rss.cbc.ca/lineup/canada-montreal.xml
- Global News Tech : https://globalnews.ca/tech/feed/

**Bonus Points** 
- Bonus points if you create another service that will scrape cbc's main web page and extract articles information and store it (dont overdo it - you dont want to get blacklisted, just build it and run it once during the demo to show how it would work)

# Exercise 2 : Data Store
As data is received from the services in Exercise 1, it should be curated and stored. 
1. Select a storage engine and design a storage schema according to the expected use as described in *Exercise 3*
2. Keep in mind the following requirements : 
    - There would be many services posting concurently from different sources (imagine 100s of feeds like the ones in *Exercise 1*)
    - Later use of the stored data will be to be retrieved as described in *Exercise 3*

**Bonus Points**
- Can you show how your API reacts to important load (load testing with fake data)?

# Exercise 3 : Retrieve API
Create an API to retrieve the stored data from *Exercise 2*.  
- Search should be allowed by author, and/or keywords (categories) and ideally by time periods.  
- Requests to the API should require authentication
- API should return the arguments passed as well as a list of articles fitting the parameters

**Bonus Points** 
- Bonus points for an async service

# Exercise 4 : Monitoring
1. Monitor the health status of your services from previous exercises
2. Create an alerting system if the services go down or requests take longer than expected

# Exercise 5 : ML Serving
The *rocket_science.py* file contains a state-of-the-art machine learning algorithm to identify whether or not the ingested article is of interest to our multiple users. Deploy this algorithm as an API, adjust its *get_article()* and *store_result()* methods to fetch the article and store the output in the storage engine chosen in *Exercise 2* for later retrieval.

```
Input :  article_id (integer) : Article Identifier
         user_id (integer) : User Identifier
Output : interest_level (float) : Interest level of the user regarding the article (ranges from 0 to 1)
```



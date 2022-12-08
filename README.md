# Final-project1
## The goal of the analysis
Our goal is to visualize the data from imdb by making a dashboard and use it to show the relationship between the number of movies with high quality and their rating, year, genre and popularity. We assumed that a high rating is proportional to the high quality of the movie and a high number of votes is proportional to the popularity of the movie. In order to facilitate the analysis, we scraped the data of high score movies in the past 50 years into our database. 

## Data Source
Our project is based on the IMDB website, we filtered our sample into featured movies only, with ratings over 7.0, number of votes over 5000, for the time period from 1970 to 2022. By the time we'd finished, we had tracked 4,462 movies for over the past 52 years.
## Data collection method
The first component of the project needed to capture the titles, genres, directors, actors, and year of release of movies that fit our specific profile, as a basis for our trend analysis and Dashboard. Start with a filter result. The result contains the movie information that matches the conditional parameters we set. The first script is designed to get all the information that meets the criteria, getting the name of the movie, the genre of the movie, the director, and the actors. The information includes specific ratings but not the comment of films. This data is then uploaded to a database that we have built on the Google Cloud platform. Util scripts are used to connect to databases and process existing data in a format that can be visualized. The app script is used to connect the processed data to index.html. We designed this page with flask. The Util script and the app script will update the collated data table to the visualization page in time.

## Methodology
### 1.download the package from following website 
* https://getbootstrap.com/
* https://datatables.net/download/#bs/dt-1.12.1
### 2. imdb.py 
* Scrape all the information satisfied the criteria 
* Create_engine in imdb.py can ake sure the data will be automatically saved to the established database
### 3. util.py
* Find the data in the database and process the data
* Use connect command to connect to the database and get the data in it
* Change the string to an int format
* Process the existing conditional data and get clean data
* Process data for line chart, bar chart and pie chart in app.py. Enable app.py to map directly with this data
### 4. app.py 
* Flask is used to make the network Interface of all diagrams and connect the data processed before
* Connect the data to the designed movie information table at the bottom of dashborad
### 5. index.html
* Gerate a dashboard page and define the parameters
* Defind all the titles in movie information table
* Create a refresh function for all graphs
* Generates a slider that allows to arbitrarily change the number of votes we find
### 6. css and js 
Echarts 1 to 3 are used to define the chart parameters. Examples include column spacing and column width in the bar chart

## Description of the dashboard
On the dashboard, it displays the histogram of rating distribution and can be filtered by year and genre, which enable us to have a general look at how the ratings distribute in different years and genres. The chart also has a resize feature to merge horizontal coordinates and change the scale of vertical coordinates to ensure a clear and visible trend if the values are too small.
![histogram](https://user-images.githubusercontent.com/112587000/206250176-05636634-30e2-4d15-b930-8f9cda33deea.gif)
Secondly, here's a line graph showing the number of movies over the years. We considered the four most frequently appearing movie genres and categorized them by color. We can find out which year the good movies increased drastically, and which year fell into the trough. In addition, it can be filtered by vote number and rating score, so that we can look more closely at the distribution of the number of movies in different popularity and rating ranges over different years. 
/（gif）
Next, it shows the percentage of genres in the overall sample in form of a pie chart. We can see the percentage of genres in different cases by choosing different years, number of votes and rating intervals. 
![piechart](https://user-images.githubusercontent.com/112587000/206250785-c5025670-faf1-4c65-9b98-139e32e7a496.gif)
And you can also filter it by director. Because of our technical limitations, we need to type the director's full name correctly in order to search for the percentage of the genres.
![searchdirector](https://user-images.githubusercontent.com/112587000/206250843-56edc303-1dee-4f6b-843d-d28913a30191.gif)
Finally, here's a table with details of the overall data sample, on which you can filter for various conditions, including director names and actor names.
![detail](https://user-images.githubusercontent.com/112587000/206250917-1140a1a0-40fa-436a-9ba2-37b26cc0fe1c.gif)

## Findings
From the histogram of the rating distribution we can see that in the high rating area (7-10 points) the trend is obviously skewed right, the most dense area distribution in 7.0-7.4, after 7.5 points the number of movies began to decline rapidly, until 8.5 points after the number of movies has been few.(graph) It’s generally similar for single years and genres.(graph)

The line chart gave us some interesting findings.

In general, the number of high-quality movies are growing throughout the years.

<img width="223" alt="image" src="https://user-images.githubusercontent.com/112193353/206364467-9f557754-b121-4bed-bd97-0641c5925d74.png">
 
1973 was the first local peak of the graph, that was when God Father II was out. The number of crime movies was relatively, but consistently large around that time. Entering the 70s, restrictions on language, adult content and sexuality, and violence had loosened up, and these elements became more widespread, but also gave filmmakers room for creativity. 
 
<img width="223" alt="image" src="https://user-images.githubusercontent.com/112193353/206364517-016367a2-8c0f-4af8-b2db-ade1587656c9.png">
We observed a high portion of good movies in the mid-late 80’s, as the industry continued to enjoy the blockbuster phenomenon began in the 70’s, and the popularization of CGI helped boosted up more childhood fantasies like Star Wars and E.T.

<img width="195" alt="image" src="https://user-images.githubusercontent.com/112193353/206364645-2dca3e5a-dfc7-43d2-a583-95321e00b676.png">
The number of good movies in the 90’s soared up, and as we investigated the industry, the booming of independent filmmakers may be the reason. By the end of the decade, most studios had formed independent film divisions that would make films with artistic, edgy, or 'serious' social issues or themes, these were the major contributor to the modern definition of prestige movies.

The number of high scored movies kept rising since then, though the data was not included in our analysis, the rising number of total productions as a whole could be another reason for this trend. Two major drops in the 2000’s and 2010’s happened in 2008 and 2020, which can be easily linked to the two global crises. The pandemic almost dragged us back too the level of early 2000. (graph below)
<img width="239" alt="image" src="https://user-images.githubusercontent.com/112193353/206364687-d88eef47-01ec-4d42-880d-971b46d04f9e.png">
 

Another interesting finding is that though not obvious, but the general trend appeared to be zigzag. It’s a normal cycle for movie industry that when famous directors and actors spent a whole year making big hits, they tend to rest for a year or two and prepare for the next, and that perhaps is why we’re observing this kind of distribution.

Romance and comedy movies have very similar trend, which can be explained by the phrase “Rom-Com”, and beside of drama which basically can be used on everything, comedy seemed to be the most liked genre and of good quality. 
<img width="468" alt="image" src="https://user-images.githubusercontent.com/112193353/206364767-4f29621e-d0ab-4faf-84e1-8c09fe77127a.png">
<img width="468" alt="image" src="https://user-images.githubusercontent.com/112193353/206364785-51efba89-b5c0-4456-8246-284bb0f737c6.png">


 

 


 
## Limitation of analysis
* As we mentioned before, we assume that the number of votes is proportional to the popularity. However, older movies have been around for years and years, so the vote count is relatively more cumulative. New movies are not necessarily unknown, but the number of votes may be relatively less dominant because of the shorter period of time.
Because of time constraints, we did not make full use of the directors' and actors' information, but simply did the search function. 
We should have visualized the entire sample of movies as well to compare the analysis with high-quality movies, but due to the large sample size, we only did the analysis of high-quality movies.
* The searching engine for pie chart is only available for director, which in reaity for general movie lovers name of actors might be more familiar to them.  Additionally, we haven’t fully understood the pre-written js scripts (source files) that helped us setting up the graphic results of the website, and thus we lost some flexibility on generating and displaying the desired results.
* The constraints for good movies we adopted lacked sophistication, as imdb score, though popular and authoritative, was only one of many quality indicators, and might be too general for some hidden gems. 
* Our initial idea was to create a library for good movies, with essential information needed for audience to look for high scored work, apparently the website we created is still not detailed enough to fully serve that idea.


## Limitation of data
* The first limitation is to select good films with seven scores as the standard may not necessarily be a proper standard. The ratings at IMDB.com are from viewers with different experiences in watching films, and their own personal interests. Nearly every film gets at least a few people rating it as a 10, and a few who rate it a 1, with most people falling along that scale. The ratings are not just averaged but weighted so that some reviews count for more than others. Newer blockbuster movies, especially very popular ones, might get a lot of positive ratings at first, but then the ratings level starts to drop. Consider as well that there is no set standard for the ratings. What I would rate as 9 or 10 would likely be based on very different criteria than how someone else might rate the same film. Each person makes a different determination, making it hard to know what a 7.0 rating even means. And some films tend to get lower ratings because of their subject matter. For example, most horror films and a small number of art-house films. That doesn't mean these movies aren't good movies. So using seven scores as a criterion to select a good movie is not necessarily an appropriate criterion.
* The second limitation is that we have selected a film with more than 5,000 votes. The sample size we obtained was 4,462 films. There were 43,157 films with a rating of seven or higher over that 50-year period, if there was no limitation on the number of people who could be seen. That means we've picked out most of the films with a score above seven. While choosing films with more than 5,000 votes ensures authenticity and objectivity, it also ensures that we're choosing films with relatively large numbers of people who agree. But it certainly took some good movies out of our sample. For example, some small budget films, they will be seen by fewer people. Even if the percentage of viewers participating in the ratings is higher than that of other movies with larger audiences, the total number of viewers may still fall short of the standards we set.

## Extension of data
* When selecting the score, we can select the top 25% of all the movies in the last ten years as the sample. Because audiences' evaluation criteria for movies change over time. As people watch more and more movies (especially good movies in the IMDB "TOP250" list), the expectations of the audience will be higher and higher. So they might not give a new movie the same grade they gave a new movie 20 years ago. Using the top 25 percent of films rated in the last ten years as a sample, rather than using seven points as a criterion, can makes our conclusions more objective.
* The sample size can be expanded when selecting the number of raters. Movies with more than 1000 ratings were added to the sample. In this way, some films with small audiences can be selected. And keep the overall sample size from changing too much. Or use the number of viewers as a percentage of the total audience as a selection criterion. Because a movie rated by more people is more likely to be a good movie or a poorly rated movie. Along with the restrictions on ratings, this helps us to pick out the really good movies that fit the standard.
* We can also try to save the movie's regional information when scraping the data. This allows for analysis of changes in scores over time in different countries. Or make a visual map of the average movie score between different countries.
* Pairing with the number of productions will make the analysis more convincing, as the higer the producion, the more likely for good movies to be created.


## Extension of Analysis
* Clearly location is a key element for film selection as it involves language and culture, it would be better to include data for location of production and language to give audience a better filtering option.  Another advantage of including locations in the analysis is so that we can link different industrial shock to the displayed trends and find better explanation behind the results.
* The dominance of drama as a genre is perhaps not surprising, film marketers often complain that “Drama is not a genre”, insofar as it doesn’t give the potential audience member any clues as to what to expect. Interaction within the dataset would be helpful for our users. We can do that by building relationships between merged tables in DBEAVER, setting keys to match other relative genre to a drama type movie. 
* Tomatometer from Rotten Tomatoes would be a supplementary indicator for movie, as the score is provided by professionals in the business.


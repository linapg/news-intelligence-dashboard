# News Intelligence Dashboard

This dashboard provides the insights for the of the **MRO Aviation Market (Maintenance Repair & Overhaul)** by gathering, cleaning and classifying news data.

## How does it work?

The news data is retrieved from the Aylien API. For more information consult the [documentation](https://docs.aylien.com/newsapi/interactive-documentation/) and get a 14 days free trial.  
The Aylien API has a Jupyter Notebook guide for Python users, you can [dowload it here](https://learn.aylien.com/news_api_python_starter_guide.html).

The news data feed is automated, categorized in hot topics, products, and services. There's a further classification in the financial moves from the MRO Providers to know when there is a Joint Venture or an Acquisition. 
The news text has been processed to get unique news and eliminate the repetition that is created by having several sources repeating the same content.


![Alt text](https://github.com/linapg/news-intelligence-dashboard/blob/main/README_images/aylien.png?raw=true)

## Content

|         File       |Functionality                        |                      |
|----------------|-------------------------------|-----------------------------|
|1.automated_search.ipynb | Gets the news for the MRO Market providers
|2.categorizing.ipynb | Classifies the news into categories like financial, sustainability, maintenance, etc...            |
|3.clean_unwanted_words.ipynb |Filters news from unrelated topics and mentions|
|4.check_text_match.ipynb |Algorithm with cosine similarity to filter repeated news|

## Dashboard

To try the functionalities, click the image:  


[![](https://github.com/linapg/news-intelligence-dashboard/blob/main/README_images/news_dashboard.png?raw=true)](https://public.tableau.com/app/profile/linaperez/viz/MRO_Market_Insights_16571036680680/NewsDashboard) 

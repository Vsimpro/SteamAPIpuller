# Steam API puller
![Python package](https://github.com/Vsimpro/SteamAPIpuller/workflows/Python%20package/badge.svg)

Webcrawler that uses Steam API to pull price data from Steam market.
The applicaton has two separate parts:
- the scraper that pulls data continously, and adds the acquired data
to a SQL database.
-  webpage client, that uses flask to display the data read from the SQL 
database. 
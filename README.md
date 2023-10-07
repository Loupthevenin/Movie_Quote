# Movie Quote Project

## Introduction

The **Movie Quote** project is a web scraping application designed to collect data from the website [Kaakook](https://www.kaakook.fr). It allows users to search for movie or TV show information, including quotes, directors, release years, and more. This README provides an overview of the project and explains how to use it effectively.

## Table of Contents

- [How It Works](#how-it-works)
- [Database Methods](#database-methods)
  - [Search](#search)
  - [Search Number of Quotes](#search-number-of-quotes)
  - [Search Years](#search-years)
  - [Search Director](#search-director)
  - [View](#view)
  - [Add](#add)
  - [Delete](#delete)
  - [Run](#run)
- [Data Storage](#data-storage)

## How It Works

The Movie Quote project scrapes data from [kaakook.fr](https://www.kaakook.fr) to create a database of movie and series quotes. The following steps outline how the project functions:

1. Run the `data_collector.py` file: This script creates the initial database by collecting IDs corresponding to movies and series from the website. This database will be used to retrieve movie information later.

2. Import the `database` module into your Python interpreter.

3. Utilize the various methods available in the `database` module to interact with the data

## Database Methods

The `database` module contains several methods for interacting with the data:

### Search

Use the `search` method to search for a movie or series by its title and retrieve its corresponding ID:

```python
search("movie_title")
```
### Search Number of Quotes

Retrieve the number of quotes for a specific movie or TV show. You can specify additional filters such as type ("Film" or "Série")

```python
search_num_quotes(200)
search_num_quotes(200, types="Film")
search_num_quotes(200, types="Série")
search_num_quotes(top=10)
```

### Search Years

Search for movies released in a specific year or within a range of years.

```python
search_years(2005)
search_years(2005, sup="sup")
search_years(2005, inf="inf")
```
### Search Director

Find movies directed by a specific director.

```python
search_director("director_name")
search_director("director_name", type="Film")
search_director("director_name", type="Série")
```

### View

View all movies currently in the list.

```python
view()
```

### Add

Add one or more movie IDs to the list.

```python
add(*10)
```

### Delete

Remove one or more movie IDs from the list.

```python
delete(*10)
```

### Run

Execute the program to ave for quotes for all movies in the list and store them in a database (or remove them if they are no longer in the list).

```python
run()
```

## Data Storage

The movies, IDs and more collected by data_collector.py are stored in a JSON file named data_movies.json  
The quotes collected by the program are stored in a JSON file named data_quote.json.

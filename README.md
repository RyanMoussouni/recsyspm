# gpeg

## Recommendation system based on a graph

The goal of this project is to develop an accurate movie recommender system based on user tastes gathered from the MovieLens dataset (25M ratings). In a second time, we would like to be able to explain its decisions. The project has been made by myself and another student of my school.

## Data set 

MovieLens : https://grouplens.org/datasets/movielens/ 

## Code explaination

You can find the recommender systems source code in the rec_syst directory. Another student applied pattern mining techniques whose source code is in the pattern_mining directory. The original data set from MovieLens is first preprocessed, using SQL queries provided by the pandas library of Python. Then, a bipartite graph is built using a sparse matrix. This graph will be useful to try to explain the recommendations of the recommender system. Features (which can be customized) are also extracted from the data, to build a feature matrix that will be fed to several binary classifiers to make the recommendation.

## Recommendation

The notebook notebook.ipynb provides an exploratory data analysis of the extracted features and showcases the results of the various recommender systems.


Some figures from the notebook (please download notebook.html and display it in your browser).

## Exploratory Data Analysis

### Pair plot of the extracted features 
![image](https://user-images.githubusercontent.com/43774265/140790003-18abed94-d4fb-4324-8bc3-eb5e066c2054.png)

## Feature selection
### Chi square test the extracted features
P-values from the chi-square test on the extracted features.

<img width="387" alt="image" src="https://user-images.githubusercontent.com/43774265/140817505-20838b56-a826-4f78-9a17-a128d0885752.png">


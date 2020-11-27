# Title
Nowcasting confidence in job security using Google Trends
## Abstract
In this project, the main purpose is to investigate how Google Trends could be used to forecast the American population’s confidence that they can maintain their jobs in the near future. Results from University of Michigan’s surveys of consumers are going to be used, which provides the average person’s expected probability to lose their current job in the following 5 years. Our proposal is to extend the paper by exploring new techniques to find and select the relevant topics in Google Trends on a new dataset. The relevance of different queries will be analyzed and compared to expectations. Useful queries and corresponding data subsets are going to be used producing various forecasting models.
## Research Questions
* Could Google Trends queries improve forecasting on people’s feeling of security in their jobs ? 
* Which keywords would be useful to make these predictions ? Would this make intuitive sense ?
## Proposed dataset
Proposed dataset is the “Probability of Losing a Job During the Next 5 Years” established by University of Michigan (available at: https://data.sca.isr.umich.edu/data-archive/mine.php, table 17). It contains distinct data points for each month starting from the 2004-01 (previous data is also available, but not from Google Trends, so it is of no use) to now. For the sake of convenience, the starting date was chosen as same as in the original “Predicting the Present with Google Trends” paper [1]. 
Moreover, relevant time series of queries, provided by Google Trends, are going to be utilized. Queries to be used during the process are going to be investigated further.
## Methods
* Building a baseline regression model to forecast people’s expectation for the probability of losing a job in the next 5 years.
* Finding related Google Trends topics which may indicate our prediction.
* Adding query indexes of the Google Trends topics to our model.
* Search for useful metrics to determine the relevant query indexes that improve
model performance.
* Comparing the results of the baseline model and the model with Google Trends
  data given the metrics.
* Analyze the findings about the relevance of the queries tested.

## Proposed timeline
![Alt text](https://github.com/epfl-ada/ada-2020-project-milestone-p3-p3_datanalyzers/blob/main/timeline.png "Timeline")
## Organization within the team
* Building baseline model: Alexandre Luster
* Searching for Useful Google Trends Topics: Everyone
* Building an improved model by using Google Trends Data: Erdem Bocugoz
* Comparing the results: Baris Sevilmis
* Creating a data story: Everyone 
* Video pitch: Everyone

## References
[1] Varian, Hal & Choi, Hyunyoung. (2009). Predicting the Present with Google Trends. Economic Record. 88. 10.2139/ssrn.1659302. 

## Questions for TAs (optional)
*Add here any questions you have for us related to the proposed project.*

# Election_Analysis

## Project Overview
A Colorado Board of Election employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate  the total number of votes cast.
2. Get a complete list of condidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- SoftwareL: Python 3.7.6, Visual Studio Code, 1.64.2

## Challenge Overview
  As stated above, the election audit was preformed to find out who won the election, how the candidates performed, and the results per county. The results are as follows:
  * _Total votes cast_: 369,711
  
  * _Votes per county_:
    1. Denver: (306,056; 82.8%)
    2. Jefferson: (38,856; 10.5%)
    3. Arapahoe: (24,802; 6.7%)
  
  * _Candidate Breakdown_ (votes, percentage of total vote):
    1. Diana DeGette: (272,893, 73.8%)
    2. Charles Casper Stockham: (85,214, 23%)
    3. Raymon Anthony Doane: (11,607, 3.1%)
  
## Challenge Summary
  Though the original code was created for this specific election, the script can be used for future elections. For future elections, the file_to_load variable would have to updated with a current path to the new csv file holding the raw date (See lines 8-9 in photo one). Also, depending on the data separation in the new csv file, the "row[]" numbers would need to be updated to pull the accurate information out of the new file (See lines 48-52 in photo two).
  
  <img width="924" alt="Screen Shot 2022-03-13 at 6 14 31 PM" src="https://user-images.githubusercontent.com/99840803/158089636-41af2b4b-7982-457f-a818-572f09aad156.png">

  
  <img width="509" alt="Screen Shot 2022-03-13 at 6 23 46 PM" src="https://user-images.githubusercontent.com/99840803/158089623-404ffbd7-8f45-44ad-99cc-e171ad27cf53.png">

 

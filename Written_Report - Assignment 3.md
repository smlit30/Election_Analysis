# Python: PyPoll Challenge for Module 3

## Results

-Overview of The Module 3 Challenge - PyPoll with Python

- Overview
     The purpose of this election audit was to use python to print out the results of election by county and candidate.  The results were broken out by count and by percentage of total votes.  In our exercise this was to test our skills using python to analyze data from a csv file. 

- Results
    - Votes Cast: The total votes cast for this election was 369,711
    - Breakdown by County: 
        - Jefferson County:     38,855 Votes    ( 10.5% of the total votes cast)
        - Denver County:        306,055 Votes   (82.8% of the total votes cast)
        - Arapahoe County:      24,801 Votes    (6.7% of the total votes cast)
        - Denver County had the largest number of votes cast
    - Breakdown by Candidate:
        - Charles Stockham:     85,213 Votes    (23.0% of the total votes cast)
        - Diana Degette:        272,892 Votes   (73.8% of the total votes cast)
        - Raymon Doane:         11,606 Votes    (3.1% of the total votes cast)
        - Diana Degette had the largest numbers of votes cast.
        - See text file with breakdown in github repository as well.


-Election Audit Summary
    - To whom it may concern,
        The script that was used to provide breakdown of the votes for this election can be easily modified for use in other election and similar voting systems.  
            1 - This script is currently good for other elections regardless of number of counties and candidates as long as it is submitted in the same format as the original script (where county and candidate are in the same columns as proposed).  The script will display count and percentage of votes of all listed counties and candidates.
            2 - With some modification if there are additional columns/identifiers of breakdown i.e. income class, political party or state we could create additional breakdowns for those similar to how we have down with county and candidate.  This would require and additional with.open and for loop to create the new breakdown with similar variables created for those categories.  
            3 - If this script were to be modified so it could show the breakdown of candidate per county or county by candidate that could also be arranged.  That breakdown would require additional for loops within the existing one to show counts of county by candidate.  This would be more cumbersome of the two modifications but may provide more relevant information.  

   




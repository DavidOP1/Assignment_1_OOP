# Assignment_1_OOP
Assignment 1 in course OOP
Name: David Ehevich, ID: 212757405
Name: Liel Zilberman, ID: 212480974
Name: Najeeb Abdhalla, ID: 316436328

Explaining the problem of the assignment:
In this assignment unlike the first one , we don't receive new calls every period of time , this time we have all the calls available beforehand.
The main problem was that we thought the algorithm should be the same as in the first assignment , just now we have to iterate over a list of calls, but we found out that we have to look at this problem differently. We had to think how will we assign the best elevator when we don't have the current position.
How did we solve thie problem? by trying to stimulate the movement of the elevator just like in the online algorithm.

Explaining the algorithm:
The program iterates over each call , and on each call we itarate over all the available elevators in the given building , on each elevator we are sending it to a function in which we first add it to the list of calls of the current elevator , then we sort it , using our sort function(It's not the regular sort , our sort sorts the list according to the smallest gap between the source floor to the current floor of the elevator , then we arrange the list accordingly.) , After getting the sorted the list with the newly added call, we calculate the total travel time of the elevator including the new call , then we delete the call from the list. After doing so with each elevator the best time is kept with index of that elevator , and then we assign that call to the list of calls of the elevator. 

Class structure:



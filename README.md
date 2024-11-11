MQTT Data from California Reservoirs and Report
Steps followed for this assignment:
1. The data sets were converted to Json object files individually, totaling three Json files.
2. Separate topics were setup for each reservoir.
3. The subscriber was initiated to listen to the port for the publishing topics.
4. The Json data for each reservoir was published in the corresponding topics one topic at a time in a
consecutive manner using a for loop.
5. The published Json data was subscribed from the topics and aggregated using a single subscriber
again using for loop to toggle between topics and reconstructed data into a single csv file for
plotting purposes. (During the action of publishing and subscribing, the Json object was converted
into Json format strings as the mqtt broker does not support dictionary data type)
6. Cols Historic_average, capacity and storage were computed on the csv read pandas data frame.
7. With the final data frame, plots were created for one specific point in time across all the reservoirs
for the mutated cols.

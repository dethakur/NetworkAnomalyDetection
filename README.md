### Network Anomaly Detection

In this project we try to find anomalies in a time series network
traffic using two techniques. We first model the network traffic as
an undirected weighted graph. Using personalized page rank we
rank each IP for each day of the Network data. We try to find if
the page rank of any node changed significantly across days. A
significant increase or decrease in the rank may mean that the
node started sending too many packets or started receiving too
many packets from other servers. We model the rank of each IP in
a time series and use Mean Shift model to estimate the change
point. If we detect a change point we flag it as anomaly. We try
the algorithm on challenge network dataset. We further try the
analysis on Darpa Test Dataset and measure the prediction and
recall value over the labeled dataset. Finally we run the algorithm
on sipscan real-time dataset and try to find IP’s with anomalous
behaviors.

The dataset used was a real world dataset downloaded from [caida].

[caida]:http://www.caida.org/data/passive/sipscan_dataset.xml

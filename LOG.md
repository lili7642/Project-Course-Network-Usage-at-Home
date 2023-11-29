# PROJECT COURSE: NETWORK USAGE AT HOME

## Time Log

### Week 45
#### Thursday 9/11
We all read the corresponding information given to us, to familiarise ourself with the project goal and linguistics. Markus implemented a psuedo code for reverese DNS lookup as well as a Dataframe.

Markus: 20:00-23:00 (3 hours)


#### Friday 10/11
Got our dataset (only on Markus computer). We started familiarise ourself with the data and began looking at ways we could handle and process the data safely, which will be discussed with Mike and Martin. A Latex document were created and worked upon.

Linus: 11:00-16:00 (5 hours)
Markus: 11:00-16:00 (5 hours)
Samuel: 11:00-16:00 (5 hours)

#### Week summary:
This week we got access to the dataset and researched some classification approaches. We are leaning towards starting with reverse DNS lookup, and other services such as “whois”, but we first have to decide if these are safe to use with the dataset. 
We also wrote some simple code to read the data as a DataFrame in Python, and automate the reverse DNS lookup with the python “socket” module.
Finally, we have started writing the simple outlines and introduction for the report in LaTeX.

### Week 46
#### Monday 13/11
Safely transfered the dataset to all participants using an USB-stick and encrypted maps. Started a private Git and began creating code for reading the data as a Dataframe. More work on the report. Can't implement anything until our meeting.

Jesper: 12:00-16:00 (4 hours)
Linus: 11:30-16:00 (4.5 hours)
Markus: 12:00-16:00 (4 hours)
Samuel: 12:00-16:00 (4 hours)

#### Tuesday 14/11
Meeting with Mike and Martin. Sat with the code. Got an OK to use WhoIs and other services due to the dataset being in its third itteration aka hard to triangulate the client. Starting looking at reverse DNS lookups.

Jesper: 13:30-16:00 (2.5 hours)
Linus: 13:30-16:00 (2.5 hours)
Markus: 13:30-16:00 (2.5 hours)
Samuel: 13:30-16:00 (2.5 hours)

#### Wednesday 15/11
Continued to preprocess data. Used socket for reverse DNS lookup, and manually did some using dig. Began doing a DB-scan for clustering flows based on time. Worked on the report.

Jesper: 10:00-16:00 (6 hours)
Linus: 10:00-16:00 (6 hours)
Markus: 12:00-16:00 (4 hours)
Samuel: 10:00-17:00 (7 hours)

#### Friday 17/11
We experimented with grouping the data by time, as well as with k-means. We also merged some domain names from another file with the data.

Jesper: 4 h
Linus: 
Markus: 
Samuel: 11:00-15:00 (4 hours)

### Week 47

#### Monday 20/11
Automated DNS lookup using the python modules "ipwhois" and "socket". Resulting dataset now contains normalized timestamp in seconds, domain names and organization, in addition to original data.

Jesper: 13:00-17:30 (4.5 hours)
Linus: 13:00-17:30 (4.5 hours)
Markus: 12:30-17:30 (5 hours)
Samuel: 12:30-17:30 (5 hours)

#### Tuesday 21/11
Meeting with Mike AND Martin. Got the Gl.net router. Wrote some on the repport

Jesper: 13:00-16:30 (3.5 hours)
Linus: 13:00-16:30 (3.5 hours)
Markus: 13:00-16:30 (3.5 hours)
Samuel: 13:00-16:30 (3.5 hours)

#### Wednesday 22/11
Gathered data for classification (Without adblocker), mostly websites, only on the computer
Linus: 13:00-18:00 (5 hours)
Markus: 13:00-18:00 (5 hours)
Samuel: 13:00-18:00 (5 hours)

#### Thursday 23/11

Markus:

#### Friday 24/11
Read some articles, gathered more data (with adblocker)
Linus: 15:00-18:00 (3 hours)
Markus:
Samuel: 14:00-18:00 (4 hours)

### Week 48

#### Monday 27/11
Merged different data gathering sessions into one large file and classified it (only to correct website). Lecture with Kristina about oral presentation. Made a code to establish which ports were used and a tokenizer for domain names.

Jesper: 11:00-17:00 (6 hours)
Linus: 11:00-16:00 (5 hours)
Markus: 11:00-16:00 (5 hours)
Samuel: 11:00-17:30 (6.5 hours)

#### Tuesday 28/11
Mandatory lecture by Stefan and Maya about ethics and rapport writing. Added a first implementation of neural network that got 70% accuracy on our own dataset.

Jesper: 13:15-17:45 (4.5 hours)
Linus: 13:15-15:15 (2 hours)
Markus: 13:15-17:45 (4.5 hours)
Samuel: 13:15-17:45 (4.5 hours)

#### Wednesday 29/11
Reading on neural network performance and tuneing with different algorithems and adding a section in the report on data processing pipeline.

Jesper: 11:30-16:00 (4.5 hours)

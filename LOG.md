# PROJECT COURSE: NETWORK USAGE AT HOME

## Time Log

### Week 45

#### Thursday 9/11
We all read the corresponding information given to us, to familiarise ourself with the project goal and linguistics. Markus implemented code for reverese DNS lookup as well as a Dataframe.

#### Friday 10/11
Got our dataset (only on Markus computer). We started familiarise ourself with the data and began looking at ways we could handle and process the data safely, which will be discussed with Mike and Martin. A Latex document were created and worked upon.

#### Week summary:
This week we got access to the dataset and researched some classification approaches. We are leaning towards starting with reverse DNS lookup, and other services such as “whois”, but we first have to decide if these are safe to use with the dataset. 

We also wrote some simple code to read the data as a DataFrame in Python, and automate the reverse DNS lookup with the python “socket” module.

Finally, we have started writing the simple outlines and introduction for the report in LaTeX.

Weekly time: 20h



### Week 46

#### Monday 13/11
Safely transfered the dataset to all participants using an USB-stick and encrypted maps. Started a private Git and began creating code for reading the data as a Dataframe. More work on the report. Can't implement anything until our meeting.

#### Tuesday 14/11
Meeting with Mike and Martin. Sat with the code. Got an OK to use WhoIs and other services due to the dataset being in its third itteration aka hard to triangulate the client. Starting looking at reverse DNS lookups.

#### Wednesday 15/11
Continued to preprocess data. Used socket for reverse DNS lookup, and manually did some using dig. Began doing a DB-scan for clustering flows based on time. Worked on the report.

#### Friday 17/11
We experimented with grouping the data by time, as well as with k-means. We also merged some domain names from another file with the data.

#### Week summary:
This week we've mainly worked on finding hostnames and owners of the IPs in the dataset and looked at what the best methods for doing this is, as well as started to do grouping of flows based on the time they occured. 

We've also read up on some papers that do network traffic classification, though most of these work with data that includes more information than what we have, eg. packet payloads and such, meaning that their methods might not be applicable for what we're doing. 

We've also continued writing on the report, mainly introduction/theory.

Weekly time: 60h



### Week 47

#### Monday 20/11
Automated DNS lookup using the python modules "ipwhois" and "socket". Resulting dataset now contains normalized timestamp in seconds, domain names and organization, in addition to original data.

#### Tuesday 21/11
Meeting with Mike and Martin discussing what information we were able to extract from our analytical approch, and got an introduction on how to operate Gl.net router. Wrote some on the report.

#### Wednesday 22/11
Gathered data for classification (Without adblocker), mostly websites, only on the one stationary computer. This gathering process was time consuming and some discussion about what features might be of interest were done in parallel.

#### Thursday 23/11
Manually labeled yesterdays data from notes and processed it. Worked on the report.

#### Friday 24/11
Read some articles, gathered more data (with adblocker)

#### Weekly summary:
This week we have gotten our hands on our own netpack device and have since been working on generating and labelling our own dataset. We are working on streamlining and automating this process. We also finished integrating the ipwhois api and automated the reverse dns lookup in the code.

Weekly time: 81h



### Week 48

#### Monday 27/11
Merged different data gathering sessions into one large file and classified it (only to correct website). Lecture with Kristina about oral presentation. Made a code to establish which ports were used and a tokenizer for domain names.

#### Tuesday 28/11
Mandatory lecture by Stefan and Maya about ethics and report writing. Added a first implementation of neural network that got 60-70% accuracy on our own dataset with bag of words representation of the domain name gathered from socket.

#### Wednesday 29/11
Reading on neural network performance and tuneing with different algorithems and adding a section in the report on data processing pipeline.

#### Thursday 30/11
Attended the poster lesson, worked on ML-model. We worked on implementing confidence threshold for guesses, so that if it was only 30% confident or lower it would classify the flow as "Unknown", and duration intervals.

#### Friday 1/12
Mike gave us some information regarding the netpack, that the setting for hardware acceleration was on, and that we should turn it off to get the correct dataflow amount. This was done and we noticed that the data amounts seemed more in line with what should be expected. Some preperations were done for next weeks data gathering and discussed if activities should be classified as well.

#### Weekly summary:
This week we've implemented classification with neural networks, so far we've only used some small and basic networks, yet achieved about 70% accuracy in the classification on our own generated data. Further work on the report has also been made.

Weekly time: 86h



### Week 49

#### Monday 4/12
We gathered more data, now with hardware acceleration off, and to save time we did this simultanously with multiple devices to gather more flows.

#### Tuesday 5/12
Meeting with Martin and Mike discussing our implementation of our model, and if it was still viabile for the project plan. Discussed some observations made on our labeled data and came to the conclusion that the more data the marrier. Mike recommended that more data should be gathered and acknowledged the time consumption it required.

#### Wednesday 6/12
We continued to gather data in accordance to Mike's suggestion. Using multiple devices it was hard to work on other tasks in parallel. Mike gave us more information about the 8 day dataset regarding what service subscriåptions the household had as well as the usage of VPN.

#### Thursday 7/12
Gathered more data, while working on script and power point for our upcoming practice presentation.

#### Friday 8/12
Worked on the presentation. We also recieved information from Martin about iOS app privacy report which include network information which might be useful for us. Markus looked into it more using his iPad.

#### Weekly summary: 
This week we've continued collecting data for a bunch of different services, we've also  continued writing on the report and created the presentation for our presentation practice on Monday. We've also experimented with creating neural networks for classification with Meta's AI-framework PyTorch, though we've not been able to increase the accuracy of the classification from 70%, which we think might be because of unsufficient data amounts. We'll keep collecting more data and see if we can improve it, and also try larger models to see if that will improve accuracy.

We noticed that the privacy report from iOS (on an iPad) that reports the hostnames that different apps and websites has connected to would report sites such as "somethingsomething.googlevideo.com" and also "ad.doubleclick.net" and "googleads.g.doubleclick.net" etc. when using Youtube both from the app and from the web browser. But when connecting the iPad to the tracking router and collecting the Youtube-flows from the iPad, the hostnames from doing reverse DNS lookup are all of the "1e100.net"-type. Hence this iOS-feature might not be as useful as we thought, we will continue and investigate next week to see if other services also report different hostnames in the iOS-report compared to reverse DNS lookup on the netflow-IPs.

Weekly time: 105h

### Week 50
#### Monday 11/12
Practice presentation with Kristina and Stefan. Worked on the report and implemented a neural network using pytorch instead.

#### Tuesday 12/12
Worked on the report and sent the outline to Martin for feedback. Also discussed and analysed the feasability and workload of implementing some sort of grouping of our datapoints.

#### Wednesday 13/12
Report writing and analysed the data from our labeled data with the 8 days data to see if there existed any trends.

#### Thursday 14/12
Zoom meeting with Martin, discussing clustering and grouping, and the end of project. Martin also thinks the grouping approch might be a project in of itself. Worked on the model. Martin also wanted us to fix some plots and text for his project funders.

#### Friday 15/12
Jesper worked on trying to gather some insightful plots for Martin. We also worked on the report with Martins feedback as well as the model.

#### Weekly summary:
This week we've gathered some more data, and we have done some preparatory work for the presentation. Some minor ideas for the poster have been made as well as some corrections of the report, in guidance to Martin's feedback.

This week has mainly been focused on analysing the data in accordance with our project goal on how to work with it moving forward. We came to the resolution that clustering and grouping might be a completely new project in of itself, and we will focus on non-internal flows (if possible we are going to double check with Mike next week) as well as extremely simple grouping of data points.

Weekly time: 71h

### Week 51

#### Monday 18/12
Worked on making the preprocessing code universal for all input NetFlow-data. Wrote on the report. Compared reverse DNS lookup output to previous output and reliesed it has changed, might be problematic with our ML-approch.

#### Tuesday 19/12
Fixed some issues with the universal code and implemented the training model for the new output gathered. Worked on the report.

#### Wednesday 20/12
Worked on the training model. It is working, and now the hyper parameters has to be tuned. With this larger dataset we got around 65% accuracy. Worked on the report.




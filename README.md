# RedditCommentAnalyser
This is a simple python project which scrapes top level comments from Reddit, performs basic sentiment analysis along with emotion detection and generates two reports based on the sentimentality. Made for MCAST Project Unit.

<p align="center">
  ![240278142-c8977c37-36cc-4847-9930-80c918b25e73](https://github.com/Abbentai/RedditCommentAnalyser/assets/104551802/15a20838-5bf9-48e9-9e5c-55485386eadf)
</p>

**Installation**
-----------------------------
In the case of PyCharm this can be done by opening up the IDE and navigating to the Welcome To PyCharm Window. From Here:
1) Click the Get from VCS Button
2) Copy the link of this repository inside the url window (https://github.com/Abbentai/RedditCommentAnalyser)
3) Specify the directory of the folder to clone the project to (Make sure its empty)
4) From here a popup window with the base interpereter and dependencies will display, make sure the project is using Python 3.10 and make sure the directory of the requirements.txt is in dependencies (This should automatically be done by the IDE)
5) Wait for the virtual environment to be fully created and the packages to install
6) Run RedditGUI.py

How to Use
-----------------------------
The programs requires two main sources of input, 1st being the reddit url of the post you wish to extract the comments from and the 2nd being the starting name of the reports to be generated.

Once fields are inputted the Scrape button can be clicked to scrape the comments and generate the positive and negative reports which are stored in the root folder of the project and showed in a popup window after generation. Old reports can also be loaded by clicking the Load Report button in the file pane
  
Demo Video
-----------------------------
[Youtube Link Here](https://www.youtube.com/watch?v=B3JMBYI2XFM)

Project Flow Chart
-----------------------------

<p align="center">
  <img src="![projectFlowChart drawio](https://github.com/Abbentai/RedditCommentAnalyser/assets/104551802/739ae27e-a9e7-46a4-8284-efdfaec0ee2e)">
</p>

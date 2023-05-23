# RedditCommentAnalyser
This is a simple python project which scrapes top level comments from Reddit, performs basic sentiment analysis along with emotion detection and generates two reports based on the sentimentality. Made for MCAST Project Unit.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/758289671591034910/1110545727546986526/240278142-c8977c37-36cc-4847-9930-80c918b25e73.png">
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
Youtube Link Here

Project Flow Chart
-----------------------------
![image](https://github.com/Abbentai/RedditCommentAnalyser/assets/104551802/b033e0e5-5fe8-4b4f-8dba-bd8bf734f095)

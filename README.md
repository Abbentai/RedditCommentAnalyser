# RedditCommentAnalyser
This is a simple python project which scrapes top level comments from Reddit, performs basic sentiment analysis along with emotion detection and generates two reports based on the sentimentality. Made for MCAST Project Unit.

<p align="center">
  <img src="https://github.com/Abbentai/RedditCommentAnalyser/assets/104551802/c745af2e-47ef-44ad-beca-236f221e3169">
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
  <img width="50%" height="50%" src="https://cdn.discordapp.com/attachments/931991165832659034/1230532345518624819/239742577-b033e0e5-5fe8-4b4f-8dba-bd8bf734f095.png?ex=6633a98d&is=6621348d&hm=afe687b79d3604dd4acb3aebff7285d45e1f7f1831ddaae76cdfacfe68c9664f&">
</p>


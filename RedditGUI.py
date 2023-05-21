#Libraries used
import nltk.tokenize
import praw
import re
import json
from praw.models import MoreComments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
import text2emotion as te
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import sys

#Arrays of comment with positive sentiment values
authorList = []
timeList = []
dateList = []
upvotesList = []
editedList = []
commentsList = []
emotiondictList = []
emotionList = []

#Arrays of comment with negative sentiment values
nauthorList = []
ntimeList = []
ndateList = []
nupvotesList = []
neditedList = []
ncommentsList = []
nemotiondictList = []
nemotionList = []

sentimentList = []

#GUI Variables
root = Tk()
user_input = tk.StringVar()
title_input = tk.StringVar()


#Miscellaneous Variables and Objects
subreddit = ""
fileName = ""
sentAnalyze = SentimentIntensityAnalyzer()
lemmatizer = WordNetLemmatizer()

#Logic

#Details to input for reddit api
# def getVariables():


def scrapeTopComments():
    global fileName
    global user_input
    global title_input
    #continue on this, research tkinter variables

    url = user_input.get()
    title = title_input.get()

    textEntry.config(text="Inserted url is invalid", fg="black")
    clearallRecords()

    # url = user_input
    #fileName = str(userInName)
    #count should replace this with an alt account at some point
    reddit = praw.Reddit(client_id="iPfyY6F3cfaaB7X8CZnd1g",
                         client_secret="iYpu8Iu-yNxqxIO7yKQpGmQlDpoMeA",
                         user_agent=('rscraper by /u/Abbenzo'),
                         username="Alternative-Citron-9",
                         password="mcastdoesnthavemyinfolol",)

    try:
        submission = reddit.submission(url=url)  #the usersubmitted post
    except praw.exceptions.InvalidURL:
        textEntry.config(fg="red", textvariable=user_input)
        textEntry.delete("0", "end")
        textEntry.insert(tk.END, "Inserted url is invalid")
        print("Inserted url is invalid")

        return
    print("Url to be Scraped: " + url)
    print("Title to be Scraped: " + title)

    for top_level_comment in submission.comments: #retrieves every top level comments in the post
        if isinstance(top_level_comment, MoreComments) or top_level_comment.body == "[deleted]":
            continue


        #Converts UTC timestamp of the comment into seperate date and time variables
        rDateTime = datetime.utcfromtimestamp(top_level_comment.created_utc)
        timeStr = rDateTime.strftime("%H:%M:%S")
        dateStr = rDateTime.strftime("%d/%m/%Y")

        commentBody = formatBody(str(top_level_comment.body))

        authorList.append(str(top_level_comment.author))
        timeList.append(str(timeStr))
        dateList.append(str(dateStr))
        upvotesList.append(str(top_level_comment.score))
        editedList.append(str(top_level_comment.edited))
        commentsList.append(commentBody)

        subreddit = top_level_comment.subreddit

    sentimentAnalysis(commentsList, subreddit)

def formatBody(body):

    #removing all urls within the string
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', body)
    for url in urls:
        body = body.replace(url,'')

    #removing any line breaks within the comment
    body = ''.join(body.splitlines())

    return body

def sentimentAnalysis(comments, subreddit):
    for comment in comments:
        count = 0
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #string containing punctuation symbols

        for character in comment: #checks every character in the comment to see if they match the punctuation marks and replaces them
            if character in punc:
                comment = comment.replace(character, "")

        tokenisation = nltk.tokenize.wordpunct_tokenize(comment) #tokenises comment body

        for token in tokenisation: #checks each token to see if it matches with a stop word, in the case it does that token is removed
            if token in stopwords.words('english'):
                tokenisation.remove(token)

        for token in tokenisation: #lemmisatises each token, getting each token and converting it to the root form
            token = lemmatizer.lemmatize(token)

        #sentiment analysis
        score = sentAnalyze.polarity_scores(comment)
        sentimentItem = score.popitem()

        if sentimentItem[1] > 0:
            sentimentList.append("Positive")
        elif sentimentItem[1] == 0:
            sentimentList.append("Neutral")
        else:
            sentimentList.append("Negative")

        #emotion identification
        emotionValue = te.get_emotion(comment)
        emotiondictList.append(emotionValue)
        emotionList.append(emotionValue.values())

        count += 1
    splittingRecords()

def clearallRecords():
    # removes the contents of all records
    records = [authorList, timeList, dateList, upvotesList, editedList, commentsList, emotiondictList, emotionList,
               nauthorList, ntimeList, ndateList, nupvotesList, neditedList, ncommentsList, nemotiondictList,
               nemotionList, sentimentList]
    for record in records:
        record.clear()
    print("Cleared Previous Data")


def cleariteminRecord(j):
    popList = []
    listOfLists = [authorList,timeList,dateList, upvotesList, editedList,commentsList,emotiondictList,emotionList]
    for list in listOfLists:
        popList.append(list.pop(j))
    sentimentList.pop(j)

    return popList

def addNegativeRecords(list):
    nauthorList.append(list[0])
    ntimeList.append(list[1])
    ndateList.append(list[2])
    nupvotesList.append(list[3])
    neditedList.append(list[4])
    ncommentsList.append(list[5])
    nemotiondictList.append(list[6])
    nemotionList.append(list[7])

def splittingRecords():
    global title_input
    j = 0
    while (j < len(commentsList)):
        if (sentimentList[j] == "Positive"):
            j += 1
        elif (sentimentList[j] == "Neutral"):
            cleariteminRecord(j)
        elif sentimentList[j] == "Negative":
            removedItemsList = cleariteminRecord(j)
            addNegativeRecords(removedItemsList)

    reportGeneration("Positive_Reports//" + title_input.get() + "positivereport.json", authorList, timeList, dateList, upvotesList, editedList, commentsList,"Positive",emotiondictList)
    reportGeneration("Negative_Reports//" + title_input.get() + "negativereport.json", nauthorList, ntimeList, ndateList, nupvotesList, neditedList, ncommentsList,"Negative", nemotiondictList)
    print("-" * 60)

def reportGeneration(reportName, aList, tList, dList, uList, eList, cList, senVal ,edList):
    #writes a new json file which converts dictionaries that contain the comment details into json objects and formats them

    with open(reportName, "w") as outfile:
        reportName.lower().strip()
        commentDetails = []
        for index in range(0, len(cList)):
            comment = {
                "Comment Number": index+1,
                "Author": aList[index],
                "Time Submitted": tList[index],
                "Date Submitted": dList[index],
                "Upvotes": uList[index],
                "Edited": eList[index],
                "Comment": cList[index],
                "Sentiment": senVal,
                "Emotions": edList[index]
            }
            commentDetails.append(comment)
        json.dump(commentDetails, outfile, indent=4)
    print(reportName + " is written")

# def readCSV(file):
#     #Reading the dataset
#     with open(file) as csvfile:
#         csv_reader = csv.reader(csvfile, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 commentsList.append(row[0].strip())
#                 line_count += 1

#GUI
def tableAdd(columns, records, table):
    table.column("#0", width=0, stretch=NO)
    for column in columns:
        if (column == "Comment"):
            multiplier = 100
            table.column(column, anchor=CENTER, stretch=YES, width=len(column) * multiplier)
        if (column == "Emotions"):
            multiplier = 45
            table.column(column, anchor=CENTER, stretch=YES, width=len(column) * multiplier)
        else:
            multiplier = 10
            table.column(column, anchor=CENTER, stretch=YES, width=len(column) * multiplier)


    table.heading("#0", text="", anchor=CENTER)
    for column in columns:
        table.heading(column, text=column ,anchor=CENTER)

    for record in records:
        table.insert(parent='', index='end', iid=record.get("Comment Number")-1, text='',values=(record.get("Comment Number"), record.get("Author"), record.get("Time Submitted"), str(record.get("Date Submitted")), record.get("Upvotes"), record.get("Edited"), record.get("Comment"), record.get("Sentiment"), record.get("Emotions")))


def displayJSON(file):

    try:
        print("File to be opened: " + file)
        file = open(file)
    except FileNotFoundError:
        print("File Couldn't be Loaded")
        return
    records = json.load(file)
    print("File opened succesfully")

    recordload = Toplevel(root)
    recordload.title("Reddit Comment Analyser | Viewing File")
    recordload.geometry("1400x600")
    recordload.iconbitmap("reddit.ico")

    frame = Frame(recordload)
    frame.pack(pady=10)

    scrollbarY = Scrollbar(frame)
    scrollbarY.pack(side=RIGHT, fill=Y)

    table = ttk.Treeview(frame, yscrollcommand=scrollbarY.set, height=500)
    table.pack()

    table['columns'] = ("Comment Number","Author", "Time Submitted", "Date Submitted", "Upvotes", "Edited", "Comment Body", "Sentiment", "Emotions")
    tableAdd(table['columns'],records ,table)

    table.pack()

def howToUse():
    howwin = Toplevel(root)
    howwin.title("Reddit Comment Analyser | How to Use")
    howwin.geometry("650x300")
    howwin.iconbitmap("reddit.ico")
    howTitle = tk.Label(howwin, text="How to use the program", font=('Cascadia Mono', 15))
    howTitle.pack(pady=10)
    howText = tk.Label(howwin,
                       text="The programs requires two main sources of input, 1st being the reddit url\n of the post you wish to extract the comments from and the 2nd being the\n starting name of the reports to be generated.",
                       font=('Cascadia Mono', 10))
    howText.pack(pady=10)
    howText = tk.Label(howwin,
                       text="Once fields are inputted the Scrape button can be clicked to scrape the\n comments and generate the positive and negative reports which are stored in \nthe root folder of the project and showed in a popup window after generation.\n Old reports can also be loaded by clicking the Load Report button in the \nfile pane ",
                       font=('Cascadia Mono', 10))
    howText.pack(pady=5)


def about():
    howwin = Toplevel(root)
    howwin.title("Reddit Comment Analyser | About Page")
    howwin.geometry("650x300")
    howwin.iconbitmap("reddit.ico")
    howTitle = tk.Label(howwin, text="About The Program", font=('Cascadia Mono', 15))
    howTitle.pack(pady=10)
    howText = tk.Label(howwin,
                       text="A simple reddit comment analyser.\n Nicholas Borg SWD 4.2A MCAST Project 2023",
                       font=('Cascadia Mono', 10))
    howText.pack(pady=10)

def exitbutton():
    root.destroy()

def getFile():
    filename = askopenfilename()
    displayJSON(filename)

def redirector(inputStr):
    #inserts the current line from the text box into the text area and scrolls the box to the latest line
    TextArea.insert(INSERT, inputStr)
    TextArea.see("end")

#calls function when written to terminal
sys.stdout.write = redirector

root.title("Reddit Comment Analyser")
root.geometry("600x400")

user_input = tk.StringVar()
title_input = tk.StringVar()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Report", command=getFile)
filemenu.add_command(label="Exit", command=exitbutton)

menubar.add_cascade(label="File", menu=filemenu)

optionsmenu = Menu(menubar, tearoff=0)
optionsmenu.add_command(label="How to use", command=howToUse)
optionsmenu.add_command(label="About", command=about)

menubar.add_cascade(label="Options", menu=optionsmenu)

label = tk.Label(root, text="Insert Reddit Post Link", font=('Cascadia Mono',15))
label.pack(pady=10)

textEntry = tk.Entry(root, width=80, textvariable=user_input)
textEntry.pack(pady=5)

label = tk.Label(root, text="Insert File Name", font=('Cascadia Mono',10))
label.pack(pady=10)

textEntry2 = tk.Entry(root, width=40, textvariable=title_input)
textEntry2.pack(pady=5)

button = tk.Button(root, text='Scrape', command=lambda: scrapeTopComments())
button.pack(pady=15)

label = tk.Label(root, text="Scraping Output:", font=('Cascadia Mono',10))
label.pack(pady=2)

TextArea = Text(root, width=60, height=8)
TextArea.pack()

root.config(menu=menubar)
root.iconbitmap("reddit.ico")
root.mainloop()











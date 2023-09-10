import urllib.request, json
from random import randrange
from flask import Flask, render_template, request
app = Flask(__name__) #creates an app instance

def getObject(objectIDs):

    try:
        #Get a random index of the array, grab that as objectID
        objectID = objectIDs[randrange(0 , len(objectIDs)-1)]
        #concatenate object ID to API base URL
        metObjectURL = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(objectID)
        response = urllib.request.urlopen(metObjectURL)
    except Exception as e:
        print(e)

    data = response.read()
    dict = json.loads(data)
    return dict

def getObjects():
    #URL returns a list of all object IDs accessible through API
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    objectIDs = dict["objectIDs"]
    return objectIDs

@app.route("/") #uses home url
def hello():
    #Using the met museum's public API for fun; XKCD API at end of method
    #first we get an int array of object IDs from the collection
    objectIDs = getObjects()

    #pick a random objectID from the array
    objectData = getObject(objectIDs)

    #I want to display an image, so 'reroll' until I get an item with an image
    while objectData["primaryImage"] == '':
        objectData = getObject(objectIDs)

    #Using XKCD API now
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    
    #just passing both as args
    return render_template("index.html", datum = objectData, xkcdatum = dict)

@app.route("/about") #uses about url
def about():
    #Modified so that page doesn't display "About Hello World!"
    header = ("About Me")
    return render_template("about.html", aboutHeader=header)

if __name__ == "__main__":
    app.run(debug = True) #runs in debug mode so we can make changes without restarting server
    
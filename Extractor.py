from bs4 import BeautifulSoup
import  DatabaseManager



def ExtractData():

    response = "FIFA_Men_Page.html"
    with open(response) as fp:
        soup = BeautifulSoup(fp, "html5lib")

    #print(soup.find("table").prettify())
    trs = soup.find("table").tbody.find_all("tr")
    for i in trs:
        ranking = i.find("td", {"class": "tbl-rank"}).span.text
        countryName = i.find("td", {"class": "tbl-teamname"}).a.text
        flagLink = i.find("td", {"class": "tbl-teamname"}).span.img['src']
        abbreviation = i.find("td", {"class": "tbl-teamname"}).span.img['title']
        pointsList = i.find("td", {"class": "tbl-points"}).text.split('(');
        currentPoints = pointsList[0]
        rawPoints = pointsList[1].split(')')[0]
        previousPoints = i.find("td", {"class": "tbl-prevpoints"}).span.text
        positionDifference = i.find("td", {"class": "tbl-prevrank"}).span.text
        positionMovement = i.find("td", {"class": "tbl-prevrank-icon"}).span['class'][0]
        if (positionMovement == "rank-equal"):
            positionMovement = "Equal"
        elif (positionMovement == "rank-rise"):
            positionMovement = "Up"
        elif (positionMovement == "rank-fall"):
            positionMovement = "Down"
        averagePoints = i.find("td", {"class": "tbl-points-avg"}).span.text
        confederation = i.find("td", {"class": "tbl-confederation"}).span.text
        #print(confederation)


        print(DatabaseManager.InsertData(ranking,
        countryName,
        flagLink,
        abbreviation,
        currentPoints,
        rawPoints,
        previousPoints,
        positionDifference,
        positionMovement,
        averagePoints,
        confederation))


print(DatabaseManager.SelectData())



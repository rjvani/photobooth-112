from flask import Flask, render_template
import os

app = Flask(__name__)

def createListOfPictures(baseSm, baseLg, picDir):
    listOfPics = os.listdir(picDir)
    listOfPics = list(sorted(listOfPics))[::-1]
    # map each path to full and thumbnail
    for index in range(len(listOfPics)):
        fp = listOfPics[index]
        listOfPics[index] = { 'small' : baseSm + fp, 'full' : baseLg + fp}
    return listOfPics

def getTemplatePics(baseSm='/media/small/', baseLg='/media/full/', picDir='media/small'):
    picsPerRow = 4
    listOfPics = createListOfPictures(baseSm, baseLg, picDir)
    templatePics = [ ]
    tempRow = [ ]

    # add all in directory to template pictures
    for pic in listOfPics:
        tempRow.append(pic)
        # create new row
        if len(tempRow) >= picsPerRow:
            templatePics.append(tempRow)
            tempRow = [ ]
    if len(tempRow) > 0:
        templatePics.append(tempRow)

    return templatePics

@app.route("/")
def main():
    templatePics = getTemplatePics()
    return render_template('index.html', pic_rows=templatePics)

@app.route("/og-squad")
def og():
    templatePics = getTemplatePics(baseSm='/media/og-squad/small/',
                                   baseLg='/media/og-squad/full/',
                                   picDir='media/og-squad/small')
    return render_template('index.html', pic_rows=templatePics)

if __name__ == "__main__":
    app.run()

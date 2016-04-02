from flask import Flask, render_template
import os

app = Flask(__name__)

def createListOfPictures():
    baseSm = '/media/small/'
    baseLg = '/media/full/'
    listOfPics = os.listdir('media/small')
    listOfPics = list(sorted(listOfPics))[::-1]
    # map each path to full and thumbnail
    for index in range(len(listOfPics)):
        fp = listOfPics[index]
        listOfPics[index] = { 'small' : baseSm + fp, 'full' : baseLg + fp}
    return listOfPics

@app.route("/")
def main():
    picsPerRow = 4
    listOfPics = createListOfPictures()
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

    return render_template('index.html', pic_rows=templatePics)

if __name__ == "__main__":
    app.run()

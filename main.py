from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def main():
    picsPerRow = 4
    listOfPics = os.listdir('media')
    listOfPics = map(lambda fp : '/media/' + fp, listOfPics)
    listOfPics = list(listOfPics)[::-1]
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

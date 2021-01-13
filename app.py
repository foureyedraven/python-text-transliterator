from flask import Flask, jsonify, request
from opencv_functions import save_photo_text

app = Flask(__name__)

# POST to receive a photo to get text from, and language it is
# Use opencv functions to grab text from the photo
# Return text grabbed from the photo for possible correction
@app.route("/photo", methods=["POST"])
def getTextFromPhoto():
    if request.method=='POST':
        posted_data = request.get_data()
        # data = posted_data['data']
        print(posted_data)
        # return "Hello from Photo"
        # posted_data = request.get_data()
        # save_photo_text(posted_data)
        # data = posted_data['data']
        # print(request.get_data())

        return 'OK'
        # return jsonify(str("Successfully stored  " + str(data)))




# POST to receive accepted text grabbed from photo, and desired output language
# use transliterator api to get transliteration
# return transliterated text
@app.route("/text", methods=["GET"])
def transliterateText():
    if request.method=='GET':
        return "Hello from Text"
        # posted_data = request.get_json()
        # data = posted_data['data']
        # return jsonify(str("Successfully stored  " + str(data)))



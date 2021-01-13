from flask import Flask, jsonify, request
# from opencv_functions import save_photo_text

app = Flask(__name__)

# POST to receive a photo to get text from, and language it is
# Use opencv functions to grab text from the photo
# Return text grabbed from the photo for possible correction
@app.route("/photo", methods=["POST"])
def getTextFromPhoto():
    if request.method=='POST':
        return "Hello from Photo"
        # posted_data = request.get_data()
        # data = posted_data['data']
        # print(posted_data)
        # return "Hello from Photo"
        # posted_data = request.get_data()
        # save_photo_text(posted_data)
        # data = posted_data['data']
        # print(request.get_data())

    # This code prints out the binary data of the uploaded image into the command line. Specifically, we grab that data from the POST request using the `request` library and use its function get_data() to get the image data, then print it to console. We must return 'OK', or else Flask believes there was an error when nothing was returned. 
    
    # posted_data = request.get_data()
    # print(posted_data)
    # return 'OK'


        # return 'OK'
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



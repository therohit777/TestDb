# backend.py
from flask import Flask, request, jsonify
from image_similarity import find_similar_images

app = Flask(__name__)

uploaded_images = []

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # You can save the image or process it as needed
    # For simplicity, we'll just keep the uploaded image in memory
    uploaded_images.append(file)

    return jsonify({'message': 'Image uploaded successfully'})

@app.route('/find_similar', methods=['POST'])
def find_similar():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    query_image = request.files['file']

    # You should implement the find_similar_images function based on your image similarity algorithm
    similar_images = find_similar_images(query_image, uploaded_images)

    return jsonify({'similar_images': similar_images})

if __name__ == '__main__':
    app.run(debug=True)

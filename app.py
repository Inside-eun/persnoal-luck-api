from flask import Flask, request, jsonify

app = Flask(__name__)

words = ["test"]

@app.route("/words", methods=["GET"])
def get_words():
    return jsonify({"words" : words}),200

@app.route("/words", methods=["POST"])
def add_word():
    data = request.get_json()
    if not data or "word" not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    word = data["word"]
    if word in words:
        return jsonify({"error" : "Word already exists"}),400

    words.append(word)
    return jsonify({"message": "Word added","words":words}),201

@app.route("/words/<string:word>", methods=["DELETE"])
def delete_word(word):
    if word not in words:
        return jsonify({"error" : "Word not found"}),404

    words.remove(word)
    return jsonify({"message" : "Word deleted", "words": words}),200

if __name__=="__main__":
    app.run(debug=True)
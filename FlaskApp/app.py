from flask import Flask, request, render_template 
import joblib
import numpy as np

""" Load the Trained Models """
# Initialize file path
model_path = 'model/stacking_classifier.pkl'
vetorizer_path = 'model/tfidf_vectorizer.pkl'
label_encoder_path = 'model/label_encoder.pkl'

# Print model content to check
with open(f'{model_path}', 'rb') as f:
    content = f.read()
    print(content[:100], "\n")  # Print the first 100 bytes

# Suppress the warnings

# Load model and vetorizer
model = joblib.load(model_path)
vectorizer = joblib.load(vetorizer_path)
label_encoder = joblib.load(label_encoder_path)

""" Setup Application """
# Initialize the Flask app
app = Flask(__name__, template_folder='templates')

# Define a route to test the model with new data
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(render_template('main.html'))
    
    if request.method == 'POST':
        # Get user input
        sender = request.form.get('sender') if 'sender' in request.form else ""
        email_text = request.form.get('emailText') if 'emailText' in request.form else ""
        
        # Transform the email text using the loaded vetorizer
        vectorizered_texts = vectorizer.transform([email_text])

        # Use model to predict the transformed text
        pred = model.predict(vectorizered_texts)
        pred_label = label_encoder.inverse_transform(pred)[0]

        # Check if sender is from Enron
        sender_organisation = "✅ Email is from an Enron employee." if sender.endswith("@enron.com") \
                   else "⚠️ ALERT: This email is NOT from an Enron employee."
        
        # Return the prediction result as JSON
        return render_template('main.html', 
                               predicted_result = pred_label, 
                               sender_organisation = sender_organisation)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
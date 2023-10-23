Human Disease Prediction
GitHub license

Overview
Human Disease Prediction is a machine learning project that uses transfer learning with ResNet-50 and ImageNet weights to predict various skin diseases. The project provides an easy-to-use web interface for users to upload images of skin conditions and get predictions for the following diseases:

'BA- cellulitis': 0
'BA-impetigo': 1
'FU-athlete-foot': 2
'FU-nail-fungus': 3
'FU-ringworm': 4
'PA-cutaneous-larva-migrans': 5
'VI-chickenpox': 6
'VI-shingles': 7
The application is deployed locally using Streamlit.

Project Structure
The project's structure is organized as follows:

bash
Copy code
├── app.py                   # Streamlit application source code
├── Disease_prediction.h5     # Pretrained model for disease prediction
├── requirements.txt         # Project dependencies
├── screenshots/             # Screenshots of the application
├── README.md                # This README file
Setup and Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/human-disease-prediction.git
Change to the project directory:

bash
Copy code
cd human-disease-prediction
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Usage
Start the Streamlit application:

bash
Copy code
streamlit run app.py
Access the application by opening the provided URL in your web browser.

Upload an image of the skin condition you want to predict.

Click the "Predict" button to get the disease prediction.

Screenshots
Screenshot 1
Screenshot 2

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
ResNet-50 with ImageNet weights
Streamlit for the web interface# Human-Disease-Prediction

# Customer Churn Prediction Project

This project is focused on predicting customer churn using machine learning. It consists of an interactive Streamlit web application where users can submit a form to get churn predictions for customers. The project also includes a Jupyter Notebook containing the code used to create the machine learning model. Additionally, the application is dockerized for easy deployment.

## Project Structure

├── App \
│ ├── app.py # Streamlit web application code\
│ ├── model.joblib #Model file after fine tuning\
│ ├──  requirements.txt # List of dependencies for the application\
│ └── Dockerfile # Docker configuration for the app\
├── MachineLearning\
│ ├── churn_model.ipynb # Jupyter Notebook for model creation\
│ └── data.csv # Dataset used for model training\
└── README.md # Project documentation


## App

The `App` folder contains the interactive Streamlit web application that allows users to input customer information and receive churn predictions. Users can submit a form with details like age, gender, location, subscription length, monthly bill, and total usage. The application then provides a prediction whether the customer will churn or not.

To run the application locally, navigate to the `App` directory and execute the following commands:

```sh
pip install -r requirements.txt
streamlit run app.py
```
You can also use Docker to run the application in a container:

```sh
docker build -t customer-churn-app .
docker run -p 8501:8501 customer-churn-app
```
# MachineLearning folder
The MachineLearning folder contains a Jupyter Notebook (churn_model.ipynb) that outlines the process of creating and training the machine learning model for customer churn prediction. The notebook includes data preprocessing, model selection, hyperparameter tuning, and model evaluation.

The dataset (data.csv) used for model training can be found in the same folder.

Docker
The application is dockerized for easy deployment. The Dockerfile in the App folder contains the configuration needed to build a Docker image of the Streamlit app.

Usage
Clone the repository: git clone <repository-url>
Navigate to the App folder and run the app: streamlit run app.py

For Docker:

Build the Docker image: docker build -t app.
Run the Docker container: docker run -p 8501:8501 app
Feel free to customize and enhance the project according to your needs.


pipeline {
    agent any

    environment {
        // Define the Python executable path explicitly to ensure the correct version is used.
        PYTHON_EXECUTABLE = "python3" // Replace "python3" with the appropriate Python executable name.
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Use the defined Python executable to install dependencies.
                sh "${PYTHON_EXECUTABLE} -m pip install -r requirements.txt"
            }
        }
        stage('Run Tests') {
            steps {
                sh "${PYTHON_EXECUTABLE} manage.py test"
            }
        }
        stage('Start Server') {
            steps {
                // Start the Django development server.
                sh "${PYTHON_EXECUTABLE} manage.py runserver 0.0.0.0:8000 &"
                // Sleep for a few seconds to allow the server to start before proceeding to the next steps.
                sh 'sleep 10'
            }
        }
    }
}
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
    }
}
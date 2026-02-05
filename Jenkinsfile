pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'
        }
    }

    environment {
        FLASK_ENV = "development"
        FLASK_APP = "app.py"

        DB_HOST = "localhost"
        DB_NAME = "testdb"
        DB_USER = "testuser"
        DB_PASSWORD = "testpass"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Venv') {
            steps {
                sh '''
                python --version
                python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Basic App Test') {
            steps {
                sh '''
                . venv/bin/activate
                python -c "import app; print('App import successful')"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}

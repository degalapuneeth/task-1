pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '--user root'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python --version

                    apt-get update
                    apt-get install -y python3-venv

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
}

pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
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

                    # Create venv in workspace (writable)
                    python -m venv venv

                    # Activate venv
                    . venv/bin/activate

                    # Upgrade pip inside venv
                    pip install --upgrade pip

                    # Install requirements
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

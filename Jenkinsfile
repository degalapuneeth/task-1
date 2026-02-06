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

                    # Install venv support (required for slim images)
                    apt-get update
                    apt-get install -y python3-venv

                    # Create virtual environment
                    python -m venv venv

                    # Activate venv
                    . venv/bin/activate

                    # Upgrade pip inside venv
                    pip install --upgrade pip

                    # Install dependencies
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

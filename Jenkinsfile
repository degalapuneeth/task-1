pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version || python --version
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Basic App Test') {
            steps {
                sh '''
                    python3 -c "import app; print('App import successful')"
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


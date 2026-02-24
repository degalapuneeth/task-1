pipeline {
    agent any

    environment {
        APP_NAME = "login-app"
    }

    stages {

        stage('Build & Deploy') {
            steps {
                script {
                    sh '''
                    echo "Stopping old containers..."
                    docker-compose down || true

                    echo "Building and starting containers..."
                    docker-compose up -d --build
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    sh '''
                    echo "Checking running containers..."
                    docker ps
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Deployment Successful 🚀"
        }
        failure {
            echo "Deployment Failed ❌"
        }
    }
}
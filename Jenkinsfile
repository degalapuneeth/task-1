pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/degalapuneeth/task-1.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh '''
                echo "Stopping old containers..."
                docker-compose down || true

                echo "Building and starting containers..."
                docker-compose up -d --build
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Running containers:"
                docker ps
                '''
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
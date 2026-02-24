pipeline {
    agent any

    stages {

        stage('Build & Deploy') {
            steps {
                withCredentials([file(credentialsId: 'env-id', variable: 'ENV_FILE')]) {
                    sh '''
                    echo "Copying .env file..."
                    cp $ENV_FILE .env

                    echo "Stopping old containers..."
                    docker compose down || true

                    echo "Building and starting containers..."
                    docker compose up -d --build
                    '''
                }
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
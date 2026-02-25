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
                    docker-compose down --remove-orphans || true

                    echo "Building and starting containers..."
                    docker-compose up -d --build --force-recreate
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Running containers:"
                docker ps

                echo "Checking application logs..."
                docker-compose logs app --tail=20
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
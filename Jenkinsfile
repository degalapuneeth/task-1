pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/degalapuneeth/task-1.git'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }
}

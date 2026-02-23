pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/degalapuneeth/task-1.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t login-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f login-app || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name login-app login-app:latest'
            }
        }
    }
}

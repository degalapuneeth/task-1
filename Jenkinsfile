pipeline {
    agent any

    environment {
        FLASK_ENV = "development"
        FLASK_APP = "app.py"

        // Dummy DB values for Jenkins run
        DB_HOST = "localhost"
        DB_NAME = "testdb"
        DB_USER = "testuser"
        DB_PASSWORD = "testpass"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Venv') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                python --version
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

    //     stage('Run Python Application') {
    //         steps {
    //             sh '''
    //             . venv/bin/activate
    //             echo "Starting Flask application..."
    //             python app.py &
    //             sleep 5
    //             echo "Flask app started successfully"
    //             '''
    //         }
    //     }
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

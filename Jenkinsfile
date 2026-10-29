pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t uat-hello-app .'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'docker run --rm uat-hello-app pytest -v'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm uat-hello-app'
            }
        }
    }
}
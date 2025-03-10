pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: "https://github.com/UMukMin/BackEnd.git"
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building images..."'
                sh 'docker-compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Stopping old container..."
                docker-compose down

                echo "Starting new container..."
                docker-compose up -d

                '''
            }
        }
    }
}
pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
                git url:'' , branch:'main'
            }
        }
        stage ('install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage ('unitest') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
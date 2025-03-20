pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
                git url:'https://github.com/praveenpeddapotula/python-project.git' , branch:'main'
            }
        }
        stage ('install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage ('unitest') {
            steps {
                sh 'python3 -m xmlrunner discover -o test-reports'
            }
        }
    }
    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
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
        stage ('package') {
            steps {
                sh 'python3 setup.py sdist bdist_wheel'
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
            junit 'test-reports/*.xml'
        }
    }
}
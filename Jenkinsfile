pipeline {
  agent any
  environment {
    token = ''
  }
  stages {
    stage('getToken') {
      steps {
        token = sh 'python getToken.py'
      }
    }
  }
}
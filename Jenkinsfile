pipeline {
  agent any
  stages {
    stage('getToken') {
      steps {
        sh 'python getToken.py'
        token = readFile(file: '.tokenID')
      }
    }
    stage('provision VM') {
      steps {
        sh 'echo ${token}'
      }
    }
  }
  environment {
    token = ''
  }
}
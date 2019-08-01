pipeline {
  agent any
  stages {
    stage('getToken') {
      steps {
        sh 'python getToken.py'
        readFile(file: '.tokenID', encoding: 'token')
      }
    }
    stage('provision VM') {
      steps {
        sh "echo ${token}"
      }
    }
  }
  environment {
    token = ''
  }
}
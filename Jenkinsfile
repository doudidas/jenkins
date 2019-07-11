pipeline {
  agent any
  stages {
    stage('getToken') {
      steps {
        sh 'python getToken.py'
      }
    }
    stage('provision VM') {
      steps {
        sh 'python requestVM.py'
      }
    }
  }
  environment {
    token = ''
  }
}
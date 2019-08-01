pipeline {
  agent any
  stages {
    stage('getToken') {
      steps {
        sh 'token=$(python getToken.py)'
      }
    }
    stage('provision VM') {
      steps {
        sh 'echo ${token}'
      }
    }
  }
}
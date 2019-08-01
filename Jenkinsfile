
pipeline {
  agent any
    environment { 
        token = ''
    }
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
}
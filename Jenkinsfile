
pipeline {
  agent any
    environment { 
        token = ''
    }
  stages {
    stage('getToken') {
      steps {
        sh 'python getToken.py'
        token = readFile('.tokenID').trim()
      }
    }
    stage('provision VM') {
      steps {
        sh "echo ${token}"
      }
    }
  }
}
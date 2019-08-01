
pipeline {
  agent any
    environment { 
        token = ''
    }
  stages {
    stage('getToken') {
      steps {
        token = sh(script: 'python getToken.py', returnStdout: true).trim()
      }
    }
    stage('provision VM') {
      steps {
        sh "echo ${token}"
      }
    }
  }
}
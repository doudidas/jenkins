pipeline {
  agent any

  parameters {
      string(name: 'token', defaultValue: '')
  }  
  stages {
    stage('getToken') {
      steps {
        token = sh 'python getToken.py'
      }
    }
    stage('provision VM') {
      steps {
        sh 'python requestVM.py ${token}' 
      }
    }
  }
  environment {
    token = ''
  }
}
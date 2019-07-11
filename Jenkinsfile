pipeline {
  agent any

  parameters {
      string(name: 'token', defaultValue: '')
  }  
  stages {
    stage('getToken') {
      steps {
        token = sh(returnStdout: true, script: "python getToken.py").trim()
      }
    }
    stage('provision VM') {
      steps {
        sh "python requestVM.py ${token}"
      }
    }
  }
}
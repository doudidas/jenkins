pipeline {
  agent any

  parameters {
      string(name: 'token', defaultValue: '')
  }  
  stages {
    stage('getToken') {
      steps {
        sh "python getToken.py"
        // sh(returnStdout: true, script: "python getToken.py").trim()
      }
    }
    stage('provision VM') {
      steps {
        sh "python requestVM.py ${token}"
      }
    }
  }
}
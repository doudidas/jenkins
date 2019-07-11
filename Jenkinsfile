pipeline {
  agent any
  stages {
    stage('getToken') {
      steps {
        sh '''ls
python getToken.py'''
        sleep 1
      }
    }
  }
}
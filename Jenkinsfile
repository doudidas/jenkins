pipeline {
  agent any
  stages {
    stage('getToken') {
      steps {
        script {
          python getToken.py
          env.token = readFile(file: '.tokenID')
        }

      }
    }
    stage('provision VM') {
      steps {
        sh 'echo ${token}'
      }
    }
  }
  environment {
    token = ''
  }
}
pipeline {
  agent any

  parameters {
      string(name: 'token', defaultValue: 'MTU2MjgzOTU3MzcyNTowNGFiZWExMzE0YmZlNDdmNzEzOTp0ZW5hbnQ6dnNwaGVyZS5sb2NhbHVzZXJuYW1lOmV0b3BpbkB2c3BoZXJlLmxvY2FsZXhwaXJhdGlvbjoxNTYyODY4MzczMDAwOjhjYmJlMzhiMmMyMjBhMWYyMWI0NGRlNDQ1NGFlODE2MWM1NzY1MTU0MzgzZjJhNTRhZDc4YmFjZDE5MDY4Y2U5MGIxYWI5ZDQyN2M2ZTUxMTdlYzhlNGJiNzMwNjY1MGU5OWU3ZjNiNTFlMWM5YjNlZDIwZDQ3N2UyZGMwMTdl')
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
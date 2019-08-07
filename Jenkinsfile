def token = ''
def locationURL = ''
pipeline {
  agent any
  environment {
    fqdn    = "cava-n-80-154.eng.vmware.com"
    centos  = 'payloads/blueprint1.json'
    destroy = 'payloads/destroyDeployment.json'
  }
  stages {
    stage('getToken') {
      steps {
        script {
          token = sh(returnStdout: true, script: 'python getToken.py ${fqdn}')
        }
      }
    }
    stage('provision VM') {
      steps {
        script {
          locationURL = sh(returnStdout: true, script: 'python requestCatalogItem.py ${fqdn} ${centos}')
        }
      }
    }
    stage('Wait Provisioning Centos') {
      steps {
        sh "python waitForRequest.py ${locationURL}"
      }
    }
    stage('get DeploymentID') {
      steps {
        sh 'python getDeploymentFromRequest.py ${fqdn}'
      }
    }
    stage('Destroy VM') {
      steps {
        script {
          locationURL = sh(returnStdout: true, script: 'python requestAction.py ${fqdn} ${destroy}')
        }
      }
    }
    stage('Wait Destroy Centos') {
      steps {
        sh "python waitForRequest.py ${locationURL}"
      }
    }
  }
}
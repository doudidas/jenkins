def token        = ''
def requestID    = ''
def deploymentID = ''

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
          requestID = sh(returnStdout: true, script: 'python requestCatalogItem.py ${fqdn} ${centos} ${token}')
        }
      }
    }
    stage('Wait Provisioning Centos') {
      steps {
        sh "python waitForRequest.py ${fqdn} ${requestID} ${token}"
      }
    }
    stage('get DeploymentID') {
      steps {
        script {
          deploymentID = sh(returnStdout: true, script: 'python getDeploymentFromRequest.py ${fqdn} ${requestID} ${token}')
        }
      }
    }
    stage('Destroy VM') {
      steps {
        script {
          locationURL = sh(returnStdout: true, script: 'python requestAction.py ${fqdn} ${destroy} ${token}')
        }
      }
    }
    stage('Wait Destroy Centos') {
      steps {
        sh "python waitForRequest.py ${fqdn} ${requestID} ${token}"
      }
    }
  }
}
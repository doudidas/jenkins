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
        sh 'python getToken.py ${fqdn}'
      }
    }
    stage('provision VM') {
      steps {
        sh 'python requestCatalogItem.py ${fqdn} ${centos}'
      }
    }
    stage('Wait for request') {
      steps {
        sh 'python waitForRequest.py'
      }
    }
    stage('get DeploymentID') {
      steps {
        sh 'python getDeploymentFromRequest.py ${fqdn}'
      }
    }
    stage('get resourceOperation') {
      steps {
        sh 'python getDeploymentFromRequest.py ${fqdn}'
      }
    }
    stage('Destroy VM') {
      steps {
        sh 'python requestAction.py ${fqdn} ${destroy}'
      }
    }
    stage('Wait for request') {
      steps {
        sh 'python waitForRequest.py'
      }
    }
  }
}
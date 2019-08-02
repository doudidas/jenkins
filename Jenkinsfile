pipeline {
  agent any
  environment {
    businessGroupID = 'b3a2dc51-5267-410c-87f3-ddfefc1645a7'
    catalogID       = '8b0c1cca-2678-470d-ab27-05f7c8a9fc21'
    payloadFilePath = 'payloads/blueprint1.json'
    fqdn = "cava-n-80-154.eng.vmware.com"
  }
  stages {
    stage('getToken') {
      steps {
        token = sh 'python getToken.py ${fqdn}'
      }
    }
    stage('provision VM') {
      steps {
        sh 'python requestCatalogItem.py ${fqdn} ${payloadFilePath} ${catalogID} ${businessGroupID}'
      }
    }
    stage('Wait for request') {
      steps {
        sh 'python waitForRequest.py'
      }
    }
  }
}
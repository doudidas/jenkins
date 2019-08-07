def centos       = "payloads/blueprint1.json"
def deploymentID = ""
def destroy      = "payloads/destroyDeployment.json"
def fqdn         = "cava-n-80-154.eng.vmware.com"
def requestID    = ""
def tokenID      = ""
pipeline {
  agent any
  stages {
    stage("getToken") {
      steps {
        script {
          tokenID = sh(returnStdout: true, script: "python getToken.py ${fqdn}").trim()
        }
      }
    }
    stage("provision VM") {
      steps {
        script {
          requestID = sh(returnStdout: true, script: "python requestCatalogItem.py ${fqdn} ${centos} ${tokenID}").trim()
        }
      }
    }
    stage("Wait Provisioning Centos") {
      steps {
        sh "python waitForRequest.py  ${fqdn} ${requestID} ${tokenID}"
      }
    }
    stage("get DeploymentID") {
      steps {
        script {
          deploymentID = sh(returnStdout: true, script: "python getDeploymentFromRequest.py ${fqdn} ${requestID} ${tokenID}").trim()
        }
      }
    }
    stage("Destroy VM") {
      steps {
        script {
          requestID = sh(returnStdout: true, script: "python requestAction.py ${fqdn} ${deploymentID} ${destroy} ${tokenID}").trim()
        }
      }
    }
    stage("Wait Destroy Centos") {
      steps {
        script {
          sh(returnStdout: true, script: "python waitForRequest.py ${fqdn} ${requestID} ${tokenID}")
        }
      }
    }
  }
}
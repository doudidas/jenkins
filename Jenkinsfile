def centos       = "payloads/blueprint1.json"
def deploymentID = ""
def destroy      = "payloads/destroyDeployment.json"
def fqdn         = "cava-n-80-154.eng.vmware.com"
def requestID    = ""
def tokenID      = ""
def ctx = {}
pipeline {
  agent any
  stages {
    stage("getToken") {
      steps {
        script {
          ctx.tokenID = sh(returnStdout: true, script: "python getToken.py ${fqdn}")
        }
      }
    }
    stage("provision VM") {
      steps {
        script {
          requestID = sh(returnStdout: true, script: "python requestCatalogItem.py ${fqdn} ${centos} ${ctx.tokenID}")
        }
      }
    }
    stage("Wait Provisioning Centos") {
      steps {
        sh "python waitForRequest.py ${fqdn} ${requestID} ${tokenID}"
      }
    }
    stage("get DeploymentID") {
      steps {
        script {
          deploymentID = sh(returnStdout: true, script: "python getDeploymentFromRequest.py ${fqdn} ${requestID} ${tokenID}")
        }
      }
    }
    stage("Destroy VM") {
      steps {
        script {
          locationURL = sh(returnStdout: true, script: "python requestAction.py ${fqdn} ${destroy} ${tokenID}")
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
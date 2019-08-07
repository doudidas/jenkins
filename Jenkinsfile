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
          ctx.requestID = sh(returnStdout: true, script: "python requestCatalogItem.py ${fqdn} ${centos} ${ctx.tokenID}")
        }
      }
    }
    stage("Wait Provisioning Centos") {
      steps {
        sh "python waitForRequest.py ${ctx.tokenID} ${fqdn} ${ctx.requestID} "
      }
    }
    stage("get DeploymentID") {
      steps {
        script {
          ctx.deploymentID = sh(returnStdout: true, script: "python getDeploymentFromRequest.py ${fqdn} ${ctx.requestID} ${ctx.tokenID}")
        }
      }
    }
    stage("Destroy VM") {
      steps {
        script {
          locationURL = sh(returnStdout: true, script: "python requestAction.py ${fqdn} ${ctx.deploymentID} ${destroy} ${tokenID}")
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
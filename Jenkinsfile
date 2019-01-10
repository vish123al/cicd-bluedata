//def gitCommit() {
  //  sh "git rev-parse HEAD > GIT_COMMIT"
    //def gitCommit = readFile('GIT_COMMIT').trim()
    //sh "rm -f GIT_COMMIT" this is for reviewboard
    //return gitCommit,,
//}

import java.text.SimpleDateFormat
jobName = "WebApp"
def dateFormat = new SimpleDateFormat("yyyyMMddHHmm")
def date = new Date()
def timestamp = dateFormat.format(date).toString()

def status= true
def TicketNumber
def output
def comment
def result
def err
def buildstatus
def committerEmail
node {

    // Checkout source code from Gitv.....
   if (status){
   try {
    stage 'Checkout and Create ServiceNow Ticket'
        checkout scm
      committerEmail = sh (script: 'git --no-pager show -s --format=\'%ae\'',returnStdout: true).trim()
        sh "pip install requests"
        output=sh (returnStdout: true, script: "python Integration.py --action Create -b ${env.BUILD_TAG} -e ${committerEmail}" )
        TicketNumber="${output}"
        comment="Checkout source code from Git stage is completed"
        result = sh(returnStdout:true , script: """python Integration.py --action Update -c '${comment}' -b ${env.BUILD_TAG} -t ${TicketNumber} """).trim()
        }
    catch (caughtError) { 
           err = caughtError
            currentBuild.result = 'FAILURE'
            result = sh(returnStdout:true , script: """python Integration.py --action Update -c '${err}' -b ${env.BUILD_TAG} -t ${TicketNumber} """).trim()
            buildstatus='Failed'
            result = sh(returnStdout:true , script: """python Integration.py --action Update -s ${buildstatus} -b ${env.BUILD_TAG} -t ${TicketNumber} """).trim()
            status = false
        }
    }

}

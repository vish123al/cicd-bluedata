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

   stage ('Install_Requirements') {
            steps {
                sh """
                    echo ${SHELL}
                    [ -d venv ] && rm -rf venv
                    #virtualenv --python=python2.7 venv
                    virtualenv venv
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install --upgrade pip
                    pip install -r requirements.txt -r dev-requirements.txt
                    make clean
                """
            }
        }

}

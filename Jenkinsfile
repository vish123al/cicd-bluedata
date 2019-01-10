def gitCommit() {
    sh "git rev-parse HEAD > GIT_COMMIT"
    def gitCommit = readFile('GIT_COMMIT').trim()
    sh "rm -f GIT_COMMIT"
    return gitCommit
}

node {

    // Checkout source code from Git
    stage 'Checking out scm for repository'
    checkout scm
    //stage '(TEST) unit/integration testing'
    //sh 'make test'
    stage '(BUILD) building image'
    sh """#!/usr/bin/env bash
                    set -xe
                    export PATH="/usr/local/bin:\${PATH}"
                    pip install --upgrade pip
                    pip install mypy
                    mypy clkhash --ignore-missing-imports --no-implicit-optional --disallow-untyped-calls
                """
    sh "docker build -t vishaldenge/dockerblog:${gitCommit()} ."
    sh "docker login -u vishaldenge -p 'v!sh@l123' "
    stage '(PUBLISH) Pushing the image '
    sh "docker push vishaldenge/dockerblog:${gitCommit()}"
     stage '(DEPLOY) Deploying the container'
    stage 'wb'
    sh "./helloworld-app.wb"
     

}

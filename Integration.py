#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */
pipeline {
    agent any
    options {
        buildDiscarder(
            // Only keep the 10 most recent builds
            logRotator(numToKeepStr:'10'))
    }
    environment {
        projectName = 'ProjectTemplate'
        emailTo = 'jere@arista.com'
        emailFrom = 'eosplus-dev+jenkins@arista.com'
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
    }

    stages {

        /*
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        */

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
}

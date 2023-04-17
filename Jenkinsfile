pipeline {
    agent any
    stages {
        stage('Git fetch') {
            steps {
                sh 'pwd'
                sh 'rm * -rf'
                git branch: 'main', credentialsId: '4209a604-ba5e-4e24-b3d8-8b6b74776d3e', url: 'https://github.com/Spiderinattack/Devops-AWS-Jenkins.git'
                sh 'python3 python_code.py'
            }
        }
        stage('TruffleHog') {
            steps {
                sh 'echo TruffleHog'
                sh 'pip3 install truffleHog'
                sh 'sudo chmod 777 /var/lib/jenkins/workspace/Python_Job/TruffleHog/Trufflehog_scan.py'
                sh 'sudo systemctl restart jenkins'
                sh '/var/lib/jenkins/workspace/Python_Job/TruffleHog/Trufflehog_scan.py'
            }
        }
        stage('Pylint') {
            steps {
                sh 'python3 test_pylint.py'
            }
        }
        stage('PyUnit') {
            steps {
                sh 'python3 PyUnit/PyUnit_fact_load.py'
            }
        }
        stage('Create PR for SIT') {
            steps {
                sh 'echo SIT PR'
            }
        }
        stage('Code Package and Deploy') {
            steps {
                sh 'echo code Package and Deploy'
            }
        }

    }
}

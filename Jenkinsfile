pipeline {
    agent any
    stages {
        stage('Deploy to Kubernetes') {
            steps {
                sh "./script.sh"
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl apply -k kubernetes/"
                        
                    }
                }
            }
        }
    }
}

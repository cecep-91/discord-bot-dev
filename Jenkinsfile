pipeline {
    environment {
    image = "ikubaru/discord-bot"
    registryCredential = 'ikubaru-docker'
    dockerImage = ''
    }
    agent any
    stages {
        stage('Building and Pushing Image') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage = docker.build image + ":1.$BUILD_NUMBER"
                        dockerImage.push()
                    }

                    sh '''sed -i "s/newTag.*/newTag: '1.$BUILD_NUMBER'/g" kubernetes/kustomization.yaml'''
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl apply -k kubernetes/"
                    }
                }
                sh "docker rmi $image:$1.BUILD_NUMBER"
            }
        }
    }
}

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
                        dockerImage = docker.build image + ":$BUILD_NUMBER"
                        dockerImage.push()
                    }
                }
                withCredentials([string(credentialsId: 'discordbotpat', variable: 'gitbotpat')]) {
                    git branch: 'main', url: "${gitbotpat}@github.com/cecep-91/discord-bot-cd.git"
                }
                script {
                    sh '''sed -i "s/newTag.*/newTag: '$BUILD_NUMBER'/g" kubernetes/kustomization.yaml'''
                    
                    sh 'git config --global user.email "cecepnine@gmail.com"'
                    sh 'git config --global user.name "cecep-91"'

                    sh 'git add kubernetes/kustomization.yaml'
                    sh 'git commit -m "image version $BUILD_NUMBER"'
                    sh 'git push origin main'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl apply -f "
                    }
                }
                sh "docker rmi $image:$IMAGE_VERSION"
            }
        }
    }
}

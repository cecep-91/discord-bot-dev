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
                git branch: 'main', credentialsId: 'githubpatdiscordbot', url: 'https://github.com/cecep-91/discord-bot-cd.git'
                script {
                    sh '''sed -i "s/newTag.*/newTag: '$BUILD_NUMBER'/g" kubernetes/kustomization.yaml'''
                    
                    sh 'git config --global user.email "cecepnine@gmail.com"'
                    sh 'git config --global user.name "cecep-91"'

                    sh 'git add kubernetes/kustomization.yaml'
                    sh 'git commit -m "image version $BUILD_NUMBER"'
                }
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'githubpatdiscordbot', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
                    sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/cecep-91/discord-bot-cd.git')
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl get node"
                    }
                }
                sh "docker rmi $image:$IMAGE_VERSION"
            }
        }
    }
}

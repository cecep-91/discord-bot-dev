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
                git branch: 'main', credentialsId: 'discord-bot-cd', url: 'https://github.com/cecep-91/discord-bot-cd.git'
                script {
                    sh '''sed -i "s/newTag.*/newTag: '$BUILD_NUMBER'/g" kubernetes/kustomization.yaml'''
                    
                    sh 'git config --global user.email "cecepnine@gmail.com"'
                    sh 'git config --global user.name "cecep-91"'

                    sh 'git add kubernetes/kustomization.yaml'
                    sh 'git commit -m "image version $BUILD_NUMBER"'
                }
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'discord-bot-ci', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD']]) {
                    sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/cecep-91/discord-bot-cd.git')
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                git branch: 'main', credentialsId: 'discord-bot-ci', url: 'https://github.com/cecep-91/discord-bot-ci.git'
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl apply -f application.yaml"
                    }
                }
                sh "docker rmi $image:$BUILD_NUMBER"
            }
        }
    }
}

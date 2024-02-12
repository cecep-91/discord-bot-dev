pipeline {
    environment {
    image = "10.100.1.140/dev-myproject/mynginx"
    registryCredential = 'harbor'
    dockerImage = ''
    }

    agent any

    stages {
        
        stage('Versioning') {
            steps {
                git branch: 'main', url: 'http://nginx-ci:glpat-QQC9-9qUxRtwuLMMutCT@10.1.24.246/root/nginx-ci.git'
                script {
                    env.IMAGE_VERSION = input message: 'Image versioning...', ok: 'Take this !!',
                            parameters: [
                                string(name: 'Version',
                                defaultValue: '1.',
                                description: 'Image versioning, input to your desire')]
                    sh 'ls -l'
                    sh 'sed -i "s/<h1>Nginx.*/<h1>Nginx developer version $IMAGE_VERSION/g" index.html'
                    sh 'git config --global user.email "admin@example.com"'
                    sh 'git config --global user.name "root"'
                    sh '''sed -i "s/newTag.*/newTag: '$IMAGE_VERSION'/g" kubernetes/kustomization.yaml'''
                    sh 'git add kubernetes/kustomization.yaml index.html'
                    sh 'git commit -m "image version $IMAGE_VERSION"'
                    sh 'git push origin main'
                }
            }
        }
        stage('Building and Pushing Image') {
            steps {
                script {
                    docker.withRegistry( 'http://10.100.1.140', registryCredential ) {
                        dockerImage = docker.build image + ":$IMAGE_VERSION"
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl apply -f application.yaml"
                    }
                }
                sh "docker rmi $image:$IMAGE_VERSION"
            }
        }
    }
}

pipeline {
    agent any
    stages {
        stage('Deploy to Kubernetes') {
            steps {
                sh "./script.sh"
                script {
                    withKubeConfig(credentialsId: 'kubeconfig') {
                        sh "kubectl apply -k kubernetes/"
                        sh "./check-health.sh"
                        try {
                            pod=$(kubectl get po -n discord-bot-dev | cut -d " " -f1 | grep discord-bot)
                            sh "kubectl exec -n discord-bot-dev $pod -- killall -9 python3"
                        } catch (err) {
                            echo err.getMessage()
                        }
                        sh "kubectl exec -n discord-bot-dev discord-bot-dev-0 -- pip install -r /app/requirements.txt"
                        sh "kubectl exec -n discord-bot-dev discord-bot-dev-0 -- python3 /app/bot.py"
                    }
                }
            }
        }
    }
}

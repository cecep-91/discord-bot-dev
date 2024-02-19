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
                            def pod = sh(script: 'kubectl get pod -n discord-bot-dev | cut -d " " -f1 | grep discord-bot', returnStdout: true).trim()
                            sh "kubectl exec -n discord-bot-dev $pod -- killall -9 python3"
                        } catch (err) {
                            echo err.getMessage()
                        }
                        sh "kubectl exec -n discord-bot-dev $pod -- pip install -r /app/requirements.txt"
                        sh "kubectl exec -n discord-bot-dev $pod -- python3 /app/bot.py"
                    }
                }
            }
        }
    }
}

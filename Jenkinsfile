pipeline {
    agent none 
    environment {
        registry = "jk940290/go_server"
        docker_user = "jk940290"
        docker_app = "go_server"
        GOCACHE = "/tmp"
    }
    stages {
        stage('Publish') {
            agent {
                kubernetes {
                    inheritFrom 'agent-template'
                }
            }
            steps{
                container('docker') {
                    sh 'echo $DOCKER_TOKEN | docker login --username $DOCKER_USER --password-stdin'
                    sh 'cd webui
                    sh 'docker build -t $DOCKER_REGISTRY:$BUILD_NUMBER .'
                    sh 'docker push $DOCKER_REGISTRY:$BUILD_NUMBER'
                }
            }
        }
        stage ('Deploy') {
            agent {
                node {
                    label 'deploy'
                }
            }
            steps {
                sshagent(credentials: ['cloudlab']) {
                    sh "sed -i 's/DOCKER_USER/${docker_user}/g' webui.yaml"
                    sh "sed -i 's/DOCKER_APP/${docker_app}/g' webui.yaml"
                    sh "sed -i 's/BUILD_NUMBER/${BUILD_NUMBER}/g' deployment.yaml"
                    sh 'scp -r -v -o StrictHostKeyChecking=no *.yml jk940290@155.98.37.91:~/'
                    sh 'ssh -o StrictHostKeyChecking=no jk940290@155.98.37.91 kubectl apply -f /users/lngo/webui.yaml -n jenkins'
                    sh 'ssh -o StrictHostKeyChecking=no jk940290@155.98.37.91 kubectl apply -f /users/lngo/webui-service.yaml -n jenkins'                                        
                }
            }
        }
    }
}

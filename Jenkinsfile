pipeline{
    agent {label 'main'}
    stages{
        stage('Connecting To GitHub...and Downloading Souce Code'){
            steps {
                git credentialsId: 'GitHub', url: 'https://github.com/talk2aanand/search.git'
                }
        }
        stage('Building Docker Image From Dockerfile'){
            steps {
               sh 'docker build -t jenkins:search .'
            }
        }
        stage('Tagging Image')
        {
            steps {
                sh 'docker tag jenkins:search devops190/jenkins_moka:search'
            }
        }
        stage('Pushing To DockerHub')
        {
            steps{
                withDockerRegistry(credentialsId: 'Docker-Hub', url: 'https://index.docker.io/v1/') {
    // some block 
       sh 'docker push devops190/jenkins:search'
}
             
            }
        }
    }
}

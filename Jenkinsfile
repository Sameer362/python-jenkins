pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'  // Install dependencies
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    sh 'pytest tests/'  // Run tests
                }
            }
        }
        stage('Deploy') {
    steps {
        sh 'python3 app.py'
    }
}
}
}


pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rj13371/blog_app'
            }
        }
        
        stage('Setup') {
            steps {
                // change pip explicitly to pip.exe directory if pip is not found
                bat ''' 
                   pip install -r requirements.txt
                   pip install selenium
                   '''
                   echo 'Dependencies installed'
            }
        }

        stage('Run Server') {
            steps {
                 // change python explicitly to python.exe directory if pip is not found
                bat ''' 
                   python manage.py runserver > output.txt 2>&1"
                '''
                sleep 15  // wait for server to start
                echo 'Server started'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'python manage.py test blog_app.selenium_tests.run'
                echo 'Tests finished'
            }
        }
    }
    post {
        always {
            bat ''' 
                FOR /F "tokens=5" %%A IN ('netstat -aon ^| find "8000" ^| find /I "listening"') DO taskkill /F /PID %%A
            '''
            echo 'Server started'
        }
    }
}
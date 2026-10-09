pipeline{
  agent any
  options{
    timestamps()
    skipDefaultCheckout(true)
  }
  stages{
    stage('Checkout'){
      steps{
        checkout scm
      }
    }
    stage('Check Python and Git'){
      steps{
        bat 'git --version'
        bat 'python --version'
        bat 'python -m pip --version'
      }
    }
    stage('Installing Dependencies'){
      steps{
        bat 'python -m pip install -r requirements.txt'
      }
    }
    stage('Install Playwright Browser'){
      steps{
        bat 'python -m playwright install chromium'
      }
    }
    stage('Run Automation Tests'){
      steps{
        bat 'python -m pytest tests -v -s'
      }
    }
  }
}

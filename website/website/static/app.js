let chatAppModule = angular.module('chatAppModule',['ui.router', 'ngCookies']);

chatAppModule.config(['$stateProvider','$urlRouterProvider',($stateProvider,$urlRouterProvider)=>{
    
    

    $stateProvider

    /** register state */
    .state('register',{
        url:'/register',
        templateUrl:'static/template/register.html',
        controller:'registerControl'
    })

    /** login state */
    .state('login',{
        url:'',
        templateUrl:'static/template/login.html',
        controller:'loginControl'
    })

    /** forgotPassword state */
    .state('forgotPassword',{
        url:'/forgotPassword',
        templateUrl:'template/forgotPassword.html',
        controller:'forgotPasswordControl'
    })

     /** Home state */
     .state('home',{
        url:'/home',
        templateUrl:'static/template/home.html',
    })

    $urlRouterProvider.otherwise('login');

}]);

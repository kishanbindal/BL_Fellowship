let chatAppModule = angular.module('chatAppModule',['ui.router']);

chatAppModule.config(['$stateProvider','$urlRouterProvider',($stateProvider,$urlRouterProvider)=>{
    $stateProvider

    /** register state */
    .state('register',{
        url:'/register',
        templateUrl:'template/register.html',
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

     /** forgotPassword state */
     .state('resetPassword',{
        url:'/resetPassword',
        templateUrl:'template/resetPassword.html',
        controller:'resetPasswordControl'
    })

    $urlRouterProvider.otherwise('login');
}])
chatAppModule.controller('loginControl',function($scope, $http, loginService){
    console.log('login called');

    $scope.login=function(){

        let data={
            'user_email':$scope.user_email,
            'user_password':$scope.user_password,
        }
        console.log('Login Data :',data);
        loginService.loginServiceUser(data,$scope);
    }
})
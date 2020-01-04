chatAppModule.controller('loginControl',function($scope, $http, loginService){
    console.log('login called');

    var user_email = $scope.user_email

    $scope.login=function(){

        let data={
            'user_email':$scope.user_email,
            'user_password':$scope.user_password,
        }
        console.log('Login Data :',data);
        loginService.loginServiceUser(data,$scope);
    }

    $scope.logout= function(){

        // let logoutData={
        //     'user_email': user_email
        // }

        // console.log('Logout Data : ------> ', logoutData)
        // loginService.logUserOut(data, $scope)
        loginService.logUserOut($scope)

    }
})
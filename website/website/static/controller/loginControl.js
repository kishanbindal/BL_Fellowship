chatAppModule.controller('loginControl', function($scope, $http, loginService){
    console.log('login called');

    var user_email = $scope.user_email
    //if ($scope.user_password != undefined ){
        $scope.login=function(){
            let data={
                'user_email':$scope.user_email,
                'user_password':$scope.user_password,
            }
            console.log('Login Data :',data);
            if (  data.user_email == '' || data.user_password == ''){
                alert("Username and password are required")
            }
            loginService.loginServiceUser(data,$scope);
        }
    //}else{
        //alert('Password cannot be empty');
    //    $state.go('login')
    //}

    $scope.logout= function(){

        // let logoutData={
        //     'user_email': user_email
        // }

        // console.log('Logout Data : ------> ', logoutData)
        // loginService.logUserOut(data, $scope)
        loginService.logUserOut($scope)

    }
})
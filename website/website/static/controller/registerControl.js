chatAppModule.controller('registerControl',function($scope,registerService){
    console.log('registration called');
    $scope.register=function(){
        let registerData={
            'firstName':$scope.firstName,
            'lastName':$scope.lastName,
            'emailId':$scope.emailId,
            'password':$scope.password
        }
        console.log('Register Data :',registerData);
        registerService.registerServicesUser(registerData,$scope);
    }
})
chatAppModule.controller('registerControl',function($scope,registerService){
    console.log('registration called');
    if ($scope.user_password===$scope.confirm_password){
        $scope.register=function(){
            let registerData={
                'username':$scope.user_name,
                'email':$scope.user_email,
                'password':$scope.user_password,
            }
            console.log('Register Data :',registerData);
            registerService.registerServicesUser(registerData,$scope);
        }
    }
})



// chatAppModule.controller('registerControl',function($scope,registerService){
//     console.log('registration called');
//     $scope.register=function(){
//         let registerData={
//             'user_name':$scope.user_name,
//             'user_email':$scope.user_email,
//             'user_password':$scope.user_password,
//             'confirm_password':$scope.confirm_password
//         }
//         console.log('Register Data :',registerData);
//         registerService.registerServicesUser(registerData,$scope);
//     }
// })
/**
 * forgotPassword controller
 */

chatAppModule.controller('forgotPasswordControl',function($scope,forgotPasswordService){
    console.log('forgotPassword called');

    $scope.forgotPassword=function(){

        let forgotPasswordData={

            'username':$scope.username
        }
        console.log('forgotPassword Data :',forgotPasswordData);
        forgotPasswordService.forgotPasswordServiceUser(forgotPasswordData,$scope);
    }
})
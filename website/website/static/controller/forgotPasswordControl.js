/**
 * forgotPassword controller
 */

chatAppModule.controller('forgotPasswordControl',function($scope,forgotPasswordService){
    console.log('forgotPassword called');

    $scope.forgotPassword=function(){

        let forgotPasswordData={

            'emailId':$scope.emailId
        }
        console.log('forgotPassword Data :',forgotPasswordData);
        forgotPasswordService.forgotPasswordServiceUser(forgotPasswordData,$scope);
    }
})
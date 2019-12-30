/**
 * resetPassword controller
 */

chatAppModule.controller('resetPasswordControl', function ($scope, resetPasswordService) {
    console.log('resetpassword called...');
    // console.log("Token get ",$stateParams.token)

    var token = localStorage.getItem('tokenforget')
    $scope.save = function () {

        var resetPasswordData = {
            'password': $scope.resetPassword,
            'token': token
        }
        console.log('resetpassword Data ' + resetPasswordData);
        resetPasswordService.resetPasswordServiceUser(resetPasswordData, $scope);
    }

})
chatAppModule.service('resetPasswordService',function($http,$location){

    this.resetPasswordServiceUser=function(data,$scope){
        console.log("resetPassword service ",data.token)
        let token = data.token;
        console.log("token reset service--",token);
        
        $http({
            method:'POST',
            url:'http://localhost:8000/resetPassword',
            data:data,
            headers : {token: token}
        }).then((response) =>
            {
                console.log("response in resetPassword server---",response);
                if(response.data.content==false)
                {
                    console.log('failed');
                    console.log(response);

                    $scope.login=function(){
                        alert('failed');
                    }
                }else{
                    console.log('reset password Successfully');
                    console.log(response);

                    $scope.resetPassword=function()
                    {
                        alert('reset password successfully');
                    }
                }
                $location.path('/#/login');
            }).catch((error) => {
                $scope.resetPassword=function(){
                    alert('failed...');
                }
                console.log('failed ...',error);
            });
    }
});
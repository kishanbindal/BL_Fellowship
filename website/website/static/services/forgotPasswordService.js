chatAppModule.service('forgotPasswordService',function($http,$location){

    this.forgotPasswordServiceUser=function(data,$scope){
        console.log("forgotPassword service ",data)
        $http({
            method:'POST',
            url:'http://localhost:8000/forgotPassword',
            data:data
        }).then((response) =>
            {
                console.log("response in forgotPassword server---",response);
                console.log("tokenforget--",response.data.result.token);
                
                if(response.data.content==false)
                {
                    console.log('failed');
                    console.log(response);

                    $scope.login=function(){
                        alert('failed');
                    }
                }else{
                    localStorage.setItem('tokenforget', response.data.result.token);
                    console.log('Link sent Successfully');
                    console.log(response);

                    $scope.forgotPassword=function()
                    {
                        alert('link sent successfully');
                    }
                }
                // $location.path('/#/resetPassword');
            }).catch((error) => {
                $scope.forgotPassword=function(){
                    alert('failed...');
                }
                console.log('failed ...',error);
            });
    }
});
chatAppModule.service('forgotPasswordService',function($http, $state, $location){

    this.forgotPasswordServiceUser=function(data,$scope){
        console.log("forgotPassword service ",data)
        $http({
            method:'POST',
            url:'http://localhost:8000/api/forgotpassword',
            data:data
        }).then((response) =>
            {
                if(response.data.content==false)
                {
                    console.log('failed');
                }else{

                    console.log(response);
                    alert('link sent successfully');
                    $state.go('login')

                }
            }).catch((error) => {
                console.log('failed ...',error);
            });
    }
});

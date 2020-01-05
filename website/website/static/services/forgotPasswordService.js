chatAppModule.service('forgotPasswordService',function($http,$location){

    this.forgotPasswordServiceUser=function(data,$scope){
        console.log("forgotPassword service ",data)
        $http({
            method:'POST',
            url:'http://localhost:8000/api/forgotpassword',
            data:data
        }).then((response) =>
            {
                console.log("response in forgotPassword server---",response);

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

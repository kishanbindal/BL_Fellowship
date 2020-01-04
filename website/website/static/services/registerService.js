chatAppModule.service('registerService',function($http,$location, $cookies, $state){

    console.log('token====> ',$cookies.csrftoken)

    this.registerServicesUser=function(data,$scope)
    {
        $http({
            method:'POST',
            url:'http://localhost:8000/api/register',
            data:data,
            headers:{
                "x-csrftoken" : $cookies.csrftoken,
            }
        }).then(
            function(response){
                console.log("response in register server---",response);
                
                if(response.data.content==false)
                {
                    console.log('Registration Failed');
                    console.log(response);

                    $scope.register=function(){
                        alert('Registration Failed');
                    }
                }else{
                    $state.go('login');
                }
            }).catch(function(error){
                $scope.register=function(){
                    alert('registration failed');
                }
                console.log('registration failed :',error)
            });
    }
});
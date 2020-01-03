chatAppModule.service('loginService',function($http, $location, $cookies){

    // $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    // $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    // $httpProvider.defaults.withCredentials = true;

    console.log('token====> ',$cookies.csrftoken)

    this.loginServiceUser=function(data,$scope){
        console.log("login service ",data)
        $http({
            method:'POST',
            url:'http://localhost:8000/api/login',
            data:data,
            headers: {
                "x-csrftoken" : $cookies.csrftoken,
                // 'xsrfCookieName': 'csrfmiddlewaretoken',
                // 'xsrfHeaderName': 'X-CSRFToken',
            }
        }).then((response) =>
            {
                console.log("response in login server---",response);
                console.log("token--", response.data);
                
                if(response.data === false)
                {
                    console.log('login failed');
                    console.log(response);

                    $scope.login=function(){
                        alert('login failed');
                    }
                }else{
                    console.log('response ---> ', response.data)

                    localStorage.setItem('token', response.data);
                    console.log('login Successfully');
                    console.log(response);

                    $location.path('/#/home');
                    $scope.login=function()
                    {
                        alert('login successfully');
                    }
                }
               
            }).catch((error) => {
                $scope.login=function(){
                    alert('login failed...');
                }
                console.log('Login failed ...',error);
            });
    }
});

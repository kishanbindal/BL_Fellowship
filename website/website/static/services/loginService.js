chatAppModule.service('loginService',function($http, $location, $cookies, $state){

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
                    $state.go("login")
                }else{
                  
                  localStorage.setItem('tokenforget', response.data.result.token);
                    console.log('login completed')
                    $state.go('home');

                }

            }).catch((error) => {
                alert('login failed...');
                $state.go('login')
            });
    }

    this.logUserOut = function(data, $scope){
        $http({
            method:'POST',
            url:'http://localhost:8000/api/logout',
            // data:data,
        }).then((response)=>{
            if (response.data===false){
                console.log('Logout failed')
            }else{
                $state.go('login')
            }
        })
    }
});

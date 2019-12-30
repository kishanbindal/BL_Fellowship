chatAppModule.service('loginService',function($http,$location){

    this.loginServiceUser=function(data,$scope){
        console.log("login service ",data)
        $http({
            method:'POST',
            url:'http://localhost:3000/login',
            data:data
        }).then((response) =>
            {
                console.log("response in login server---",response);
                // console.log("token--", response.data.result.token);
                
                if(response.data === false)
                {
                    console.log('login failed');
                    console.log(response);

                    $scope.login=function(){
                        alert('login failed');
                    }
                }else{

                    localStorage.setItem('token', response.data);
                    console.log('login Successfully');
                    console.log(response);

                    $location.path('');
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

// chatAppModule.service('loginService',function($http,$location){

//     this.loginServiceUser=function(data,$scope){
//         console.log("login service ",data)
//         $http({
//             method:'POST',
//             url:'http://localhost:8000/login',
//             data:data
//         }).then((response) =>
//             {
//                 console.log("response in login server---",response);
//                 console.log("token--", response.data.result.token);
                
//                 if(response.data.result.data === false)
//                 {
//                     console.log('login failed');
//                     console.log(response);

//                     $scope.login=function(){
//                         alert('login failed');
//                     }
//                 }else{

//                     localStorage.setItem('token', response.data.result.token);
//                     console.log('login Successfully');
//                     console.log(response);

//                     $scope.login=function()
//                     {
//                         alert('login successfully');
//                     }
//                 }
//                 $location.path('');
//             }).catch((error) => {
//                 $scope.login=function(){
//                     alert('login failed...');
//                 }
//                 console.log('Login failed ...',error);
//             });
//     }
//     this.goRegister=function()
// });
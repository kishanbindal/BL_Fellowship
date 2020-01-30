// chatAppModule.services('homeService', function($http,$state){

//     this.logOutUser = function($scope){
//         $http({
//             method:'POST',
//             url:'http://localhost:8000/api/logout',
//         }).then((response)=>{
            
//             if(response === false){
//                 console.log('Could Not Logout');
//             }else{
//                 console.log('logout successful');
//                 $state.go('login');
//             }
//         })
//     }

// })
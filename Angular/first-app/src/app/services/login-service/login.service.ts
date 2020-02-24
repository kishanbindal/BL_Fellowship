import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Router} from '@angular/router'
import {MatSnackBar} from '@angular/material/snack-bar'

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient, private router: Router, private _snackbar:MatSnackBar) {
    console.log('Login Service Connected');
   }

  postData(email, password){
    console.log(`Got Email : ${email}`);
    console.log(`Got Password: ${password}`);
    let data = {"email": email, "password":password};
    const headers = new HttpHeaders().set("content-type", "application/json");
    let option
    this.http.post('http://localhost:8000/fun/api/login',data, {headers})
    .subscribe((response) => {
      console.log(response)
      console.log(` response status : ${response['success']}`);
      try{
        if (response['success'] === true){
          localStorage.setItem('token', response['token']);
          this.router.navigate(['/home']);
        }else{
          console.log('Fail')
          this._snackbar.open("Unable To Login, Please Verify Credentials","exit",{
            duration:5000,  
          })
        } 
      }catch(err){
        console.log(err)
          this._snackbar.open("An Error Occured, Unable to Sign-in","exit",{
            duration:5000,});  
      }
      
    })
  }
}

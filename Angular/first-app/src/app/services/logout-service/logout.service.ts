import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class LogoutService {

  constructor(private http: HttpClient, private route: Router, private _snackbar:MatSnackBar) { }

  logUserOut(){
    let token = localStorage.getItem('token');
    this.http.post("http://localhost:8000/fun/api/logout", null, {headers: {
      "content-type": "application/json",
      "token": token,
    }})
    .subscribe((response)=> {
      console.log(`Logout Response : ${response}`)
      if (response['success'] === true){
        localStorage.removeItem('token');
        localStorage .removeItem('user');
        this.route.navigate(['']);
        this._snackbar.open("SuccessFully Logged Out", "Close", {duration:2500})
      }else{
        console.log("Something Went Wrong, Could Not Log User Out");
        this._snackbar.open("OOPS, Something Went Wrong","Close", {
          duration: 5000
        })
      }
    })
  }

}

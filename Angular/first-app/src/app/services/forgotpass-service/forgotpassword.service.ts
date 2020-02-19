import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ForgotpasswordService {

  constructor(private http: HttpClient) { } 

  postData(email:string){
    console.log(`forgot Password email : ${email}`)
    let data = {'email':email}
    const headers = new HttpHeaders().set("content-type", "application/json")
    this.http.post("http://localhost:8000/fun/api/forgotpassword", data, {headers})
    .subscribe((response)=> {
      console.log(response)
      if(response['success'] === true){
        alert(response['message']);
      }else{
        console.log('Unable to Perform Action')
      }
    })
  }
}

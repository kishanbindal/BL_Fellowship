import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) {
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
      // console.log(` response status : ${response['success']}`); 
      if (response['success'] === true){
        localStorage.setItem('token', response['token'])
        alert('Logged In Successfully.')
      }
    })
  }
}

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
    this.http.post('localhost:8000/fun/api/login',data);
  }
}

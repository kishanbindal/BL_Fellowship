import { Injectable } from '@angular/core';
import {HttpClient ,HttpHeaders} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  constructor(private http: HttpClient) {

   }

  postData(username:string, email:string, password:string, confirm_password:string){
    console.log(`Registration Data:  ${[username, email, password, confirm_password]}`);

    if (password === confirm_password){
      let data = {'username': username, 'email':email, 'password': password}
      const headers = new HttpHeaders().set('content-type', 'application/json');
      this.http.post('http://localhost:8000/fun/api/register', data, {headers})
      .subscribe((response) => {
        console.log(response);
        if (response['success'] === true){
          alert(response['message']);
        }else{
          console.log('Unsuccessful')
        }
      })
    }

  }
}

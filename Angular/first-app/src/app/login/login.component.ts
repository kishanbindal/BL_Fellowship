import { Component, OnInit } from '@angular/core';
import {LoginService} from '../services/login-service/login.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  forgotPassword:boolean;
  email:string;
  password: string;

  constructor(private ls: LoginService) { 
    
  }

  ngOnInit(): void {
    this.forgotPassword = false;
  }

  goForgotPassword(){
    console.log('Clicked on Forgot Password!')
    this.forgotPassword = true;
    console.log(this.forgotPassword)
    return this.forgotPassword;
  }

  submitData(){
    this.ls.postData(this.email, this.password);
  }

}

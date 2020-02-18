import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  forgotPassword:boolean;
  constructor() { 
    this.forgotPassword = false;
  }

  ngOnInit(): void {
  }

  goForgotPassword(){
    console.log('Clicked on Forgot Password!')
    this.forgotPassword = true;
    console.log(this.forgotPassword)
    return this.forgotPassword;
  }

}

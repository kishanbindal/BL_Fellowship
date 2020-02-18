import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-usersidebar',
  templateUrl: './usersidebar.component.html',
  styleUrls: ['./usersidebar.component.css']
})
export class UsersidebarComponent implements OnInit {

  userLogin:boolean;
  userRegister:boolean;

  constructor() {
    this.userLogin = false;
    this.userRegister = true; 
   }

  ngOnInit(): void {
  }

  goRegister(){
    this.userLogin = false;
    this.userRegister = true;
    console.log(`goRegister\nRegistration status : ${this.userRegister}`)
    console.log(`Login Status: ${this.userLogin}`)
    return this.userRegister
  }

  goLogin(){
    this.userLogin =true;
    this.userRegister = false;
    console.log(`goLogin\nRegistration status : ${this.userRegister}`)
    console.log(`Login Status: ${this.userLogin}`)
    return this.userLogin
  }
}

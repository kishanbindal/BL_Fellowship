import { Component, OnInit } from '@angular/core';
import { RegistrationService } from '../services/registration-service/registration.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  username:string;
  email:string;
  password:string;
  confirm_password:string;

  constructor(private rs : RegistrationService) { }

  ngOnInit(): void {
  }

  submitRegistrationData(){
    this.rs.postData(this.username, this.email, this.password, this.confirm_password)
  }

}

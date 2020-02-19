import { Component, OnInit } from '@angular/core';
import { ForgotpasswordService } from '../services/forgotpass-service/forgotpassword.service';

@Component({
  selector: 'app-forgot-password',
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.css']
})
export class ForgotPasswordComponent implements OnInit {

  email:string;

  constructor(private fs: ForgotpasswordService) { }

  ngOnInit(): void {
  }

  submitForgotPasswordData(){
    this.fs.postData(this.email);
  }
}

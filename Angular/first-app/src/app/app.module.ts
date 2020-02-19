import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';

//------------------Components------------------------
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { UsersidebarComponent } from './usersidebar/usersidebar.component';
import { RegisterComponent } from './register/register.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';

//-------------------Services-------------------------
import {LoginService} from './services/login-service/login.service'



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    UsersidebarComponent,
    RegisterComponent,
    ForgotPasswordComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [LoginService],
  bootstrap: [AppComponent]
})
export class AppModule { }

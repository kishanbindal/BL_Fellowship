import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import {Routes, RouterModule} from '@angular/router'

//------------------Components------------------------
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { UsersidebarComponent } from './usersidebar/usersidebar.component';
import { RegisterComponent } from './register/register.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { HeaderNavbarComponent } from './header-navbar/header-navbar.component';


//-------------------Services-------------------------
import {LoginService} from './services/login-service/login.service'
import {RegistrationService} from './services/registration-service/registration.service'
import {ForgotpasswordService} from './services/forgotpass-service/forgotpassword.service';
import { SearchComponent } from './search/search.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    UsersidebarComponent,
    RegisterComponent,
    ForgotPasswordComponent,
    HeaderNavbarComponent,
    SearchComponent,],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    BrowserAnimationsModule,
  ],
  providers: [
    LoginService,
    RegistrationService,
    ForgotpasswordService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

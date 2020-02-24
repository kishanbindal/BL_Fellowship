import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';

//------------------Angular Material------------------
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {LayoutModule} from '@angular/cdk/layout'
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatIconModule} from '@angular/material/icon';
import {MatListModule} from '@angular/material/list';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatDialogModule} from '@angular/material/dialog'

//------------------Components------------------------
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { ListviewGridviewComponent } from './listview-gridview/listview-gridview.component';
import { ProfileOptionsComponent } from './profile-options/profile-options.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { FirstpageComponent } from './firstpage/firstpage.component';

//-------------------Services-------------------------
import {LoginService} from './services/login-service/login.service'
import {RegistrationService} from './services/registration-service/registration.service'
import {ForgotpasswordService} from './services/forgotpass-service/forgotpassword.service';
import { AppRoutingModule } from './app-routing/app-routing.module';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    ForgotPasswordComponent,
    SideNavComponent,
    SearchBarComponent,
    FirstpageComponent,
    ListviewGridviewComponent,
    ProfileOptionsComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    LayoutModule,
    MatToolbarModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatButtonModule,
    MatSnackBarModule,
    MatDialogModule,
    AppRoutingModule,
  ],
  providers: [
    LoginService,
    RegistrationService,
    ForgotpasswordService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

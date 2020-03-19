import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
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
import {MatCardModule} from '@angular/material/card';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatDatepickerModule } from '@angular/material/datepicker';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatInputModule} from '@angular/material/input';
import { MatAutocompleteModule } from '@angular/material/autocomplete'

//------------------Components------------------------
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { ListviewGridviewComponent } from './listview-gridview/listview-gridview.component';
import { ProfileOptionsComponent, ProfileOptionsDialogComponent } from './profile-options/profile-options.component';
import { SideNavComponent } from './side-nav/side-nav.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { FirstpageComponent } from './firstpage/firstpage.component';
import { SingleCardComponent, SingleCardDialogComponent } from './single-card/single-card.component';
import { RemindMeComponent, ReminderDialogBoxComponent } from './remind-me/remind-me.component';
import { CollaboratorsComponent, CollaboratorsDialogBoxComponent } from './collaborators/collaborators.component';
import { ColorPickerComponent, ColorPickerDialogComponent } from './color-picker/color-picker.component';
import { ArchiveButtonComponent } from './archive-button/archive-button.component';
import { NoteSettingComponent } from './note-setting/note-setting.component';
import { AllNotesGridComponent } from './all-notes-grid/all-notes-grid.component';
import { UploadNoteImageComponent } from './upload-note-image/upload-note-image.component';
import { AddNoteComponent } from './add-note/add-note.component';
import { AllNotesPageComponent } from './all-notes-page/all-notes-page.component';
import { RemindersPageComponent } from './reminders-page/reminders-page.component';
import { RemindersGridComponent } from './reminders-grid/reminders-grid.component';
import { LabelComponent } from './label/label.component'
import { LabelDialogComponent } from './label/label.component'

//-------------------Services-------------------------
import {LoginService} from './services/login-service/login.service'
import {RegistrationService} from './services/registration-service/registration.service'
import {ForgotpasswordService} from './services/forgotpass-service/forgotpassword.service';
import { AppRoutingModule } from './app-routing/app-routing.module';
import { LogoutService } from './services/logout-service/logout.service';
import { DataService } from './services/DataService/data-service.service';
import { ArchivedNotesPageComponent } from './archived-notes-page/archived-notes-page.component';
import { ArchivedGridComponent } from './archived-grid/archived-grid.component';


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
    ProfileOptionsDialogComponent,
    SingleCardComponent,
    RemindMeComponent,
    ReminderDialogBoxComponent,
    CollaboratorsComponent,
    CollaboratorsDialogBoxComponent,
    ColorPickerComponent,
    ColorPickerDialogComponent,
    ArchiveButtonComponent,
    NoteSettingComponent,
    AllNotesGridComponent,
    UploadNoteImageComponent,
    SingleCardDialogComponent,
    AddNoteComponent,
    AllNotesPageComponent,
    RemindersPageComponent,
    RemindersGridComponent,
    ArchivedNotesPageComponent,
    ArchivedGridComponent,
    LabelComponent,
    LabelDialogComponent,
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
    MatCardModule,
    MatGridListModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatInputModule,
    MatAutocompleteModule,
    AppRoutingModule,
    ReactiveFormsModule,
  ],
  entryComponents:[
    SingleCardDialogComponent,
  ],
  providers: [
    LoginService,
    RegistrationService,
    ForgotpasswordService,
    LogoutService,
    DataService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FirstpageComponent } from '../firstpage/firstpage.component'
import { first } from 'rxjs/operators';
import { AllNotesPageComponent } from '../all-notes-page/all-notes-page.component';
import { RemindersPageComponent } from '../reminders-page/reminders-page.component';

const routes: Routes = [
  { path: '', component: FirstpageComponent },
  { path: 'home', component: AllNotesPageComponent },
  { path: 'reminders', component: RemindersPageComponent },
];

@NgModule({
  imports: [
      RouterModule.forRoot(routes)
  ],
  exports: [
      RouterModule
  ],
  declarations: [
  ]
})
export class AppRoutingModule { }

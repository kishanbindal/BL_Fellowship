import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FirstpageComponent } from '../firstpage/firstpage.component'
import { first } from 'rxjs/operators';
import { AllNotesPageComponent } from '../all-notes-page/all-notes-page.component';
import { RemindersPageComponent } from '../reminders-page/reminders-page.component';
import { ArchivedNotesPageComponent } from '../archived-notes-page/archived-notes-page.component';
import { SearchNotesPageComponent } from '../search-notes-page/search-notes-page.component';

const routes: Routes = [
  { path: '', component: FirstpageComponent },
  { path: 'home', component: AllNotesPageComponent },
  { path: 'reminders', component: RemindersPageComponent },
  { path: 'archived', component: ArchivedNotesPageComponent },
  { path: 'search', component: SearchNotesPageComponent },
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

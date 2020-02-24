import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FirstpageComponent } from '../firstpage/firstpage.component'
import { SideNavComponent } from '../side-nav/side-nav.component'
import { first } from 'rxjs/operators';

const routes: Routes = [
  { path: '', component: FirstpageComponent },
  { path: 'home', component: SideNavComponent }
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

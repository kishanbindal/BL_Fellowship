import { Component } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { Router } from '@angular/router';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.css']
})
export class SideNavComponent {

  opened:boolean;

  constructor(private router: Router) {
  }
  
  goDashboardView(){
    this.router.navigate(['/home'])
  }

  goReminderView(){
    this.router.navigate(['/reminders'])
  }

  goArchivedView(){
    console.log('Clicked on Archive View Button')
    this.router.navigate(['/archived'])
  }

}

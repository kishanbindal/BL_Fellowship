import { Component, Output, EventEmitter } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { Router } from '@angular/router';
import { DataService } from '../services/DataService/data-service.service';

@Component({
  selector: 'app-side-nav',
  templateUrl: './side-nav.component.html',
  styleUrls: ['./side-nav.component.css']
})
export class SideNavComponent {

  opened:boolean;

  @Output() sendListView = new EventEmitter(false)


  constructor(private router: Router,
    private dataService : DataService) {
      this.dataService.getAllUsers();
      this.dataService.getLabels();
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

  getListSignal($event){
    console.log('List-Grid view event in Sidenav:', $event);
    this.sendListView.emit($event)
  }

}

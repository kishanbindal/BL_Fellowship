import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reminders-page',
  templateUrl: './reminders-page.component.html',
  styleUrls: ['./reminders-page.component.css']
})
export class RemindersPageComponent implements OnInit {

  view=false

  constructor() {}

  ngOnInit(): void {
  }

  getListSignal($event){
    console.log('Event in Reminder notes grid Component : ', $event);
    this.view = $event;
  }

}

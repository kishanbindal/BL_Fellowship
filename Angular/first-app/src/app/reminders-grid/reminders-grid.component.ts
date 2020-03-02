import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';

@Component({
  selector: 'app-reminders-grid',
  templateUrl: './reminders-grid.component.html',
  styleUrls: ['./reminders-grid.component.css']
})
export class RemindersGridComponent implements OnInit {

  reminderNotes;

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.getReminders();
  } 
  
  getReminders(){
    this.dataService.reminderNotes.subscribe(data => this.reminderNotes=data)
    setTimeout(()=> console.log(this.reminderNotes), 2000);
  }

}

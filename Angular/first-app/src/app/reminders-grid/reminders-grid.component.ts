import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';

@Component({
  selector: 'app-reminders-grid',
  templateUrl: './reminders-grid.component.html',
  styleUrls: ['./reminders-grid.component.css']
})
export class RemindersGridComponent implements OnInit {

  reminderNotes;

  @Input() view

  constructor(private dataService: DataService) {
   }

  ngOnInit(): void {
    this.getReminders();
  } 
  
  getReminders(){
    this.dataService.getReminderNotes()
    this.dataService.reminderNotes.subscribe(data => {console.log(data);this.reminderNotes=data})
    setTimeout(()=> console.log(this.reminderNotes), 2000);
  }

}

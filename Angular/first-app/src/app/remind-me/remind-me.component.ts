import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-remind-me',
  templateUrl: './remind-me.component.html',
  styleUrls: ['./remind-me.component.css']
})
export class RemindMeComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openReminderDialog(){
    console.log("Opening Reminders Dialog Box");
    const dialogRef = this.dialog.open(ReminderDialogBoxComponent, {
      width: '20em',
      height: '20em',
    })

    dialogRef.afterClosed().subscribe(result => {
      console.log('Dialog Box Closed');
    })
  }
}

//ReminderDialogBox Component

@Component({
  selector: "app-reminder-dialog-box",
  templateUrl: "remind-me-dialog.component.html",
})

export class ReminderDialogBoxComponent {}

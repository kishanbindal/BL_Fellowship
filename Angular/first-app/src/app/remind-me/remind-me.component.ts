import { Component, OnInit, Output,EventEmitter } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-remind-me',
  templateUrl: './remind-me.component.html',
  styleUrls: ['./remind-me.component.css']
})
export class RemindMeComponent implements OnInit {

  @Output() sendReminder = new EventEmitter();
  reminder;

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openReminderDialog($event){
    console.log("Opening Reminders Dialog Box");
    console.log($event);
    let rect = ($event.target.getBoundingClientRect())
    let leftX = (rect.x-17.5)+'px'; console.log(leftX);
    let topY = (rect.y+40)+'px'; console.log(topY);
    const dialogRef = this.dialog.open(ReminderDialogBoxComponent, {
      width: '20em',
      height: '15em',
      position: {left: leftX, top: topY}
    })

    dialogRef.afterClosed().subscribe(result => {
      this.reminder = result
      console.log(`Data from Dialog : ${this.reminder}`);
      this.sendReminder.emit(this.reminder);
    })
  }
}

//ReminderDialogBox Component

@Component({
  selector: "app-reminder-dialog-box",
  templateUrl: "remind-me-dialog.component.html",
  styleUrls: ["remind-me-dialog.component.css"]
})

export class ReminderDialogBoxComponent {

  inputDate;
  inputTime;

  dateOutput;

  pickDate:boolean;

  constructor(public dialogRef: MatDialogRef<ReminderDialogBoxComponent>){
    this.pickDate = false;
  }

  openDateTime(){
    return this.pickDate = true;
  }

  closeDateTime(){
    if (this.inputDate != undefined && this.inputTime != undefined){
      let inputDateresult = this.inputDate.split('-'); console.log(`Split Date : ${inputDateresult}`)
    let inputTimeResult = this.inputTime.split(':'); 
    let date = new Date(inputDateresult[0], inputDateresult[1]-1, inputDateresult[2], inputTimeResult[0], inputTimeResult[1]);
    this.dateOutput = date;
    console.log(`Date Object : ${this.dateOutput}`)
    this.dialogRef.close(this.dateOutput)
    }else{
      return this.pickDate = false;
    }
  }

  save(){
    if (this.inputDate != undefined && this.inputTime != undefined){
      let inputDateresult = this.inputDate.split('-'); console.log(`Split Date : ${inputDateresult}`)
    let inputTimeResult = this.inputTime.split(':'); 
    let date = new Date(inputDateresult[0], inputDateresult[1]-1, inputDateresult[2], inputTimeResult[0], inputTimeResult[1]);
    this.dateOutput = date;
    console.log(`Date Object : ${this.dateOutput}`)
    this.dialogRef.close(this.dateOutput)
    } 
  }

}

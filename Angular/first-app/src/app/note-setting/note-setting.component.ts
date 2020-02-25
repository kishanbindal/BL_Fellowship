import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-note-setting',
  templateUrl: './note-setting.component.html',
  styleUrls: ['./note-setting.component.css']
})
export class NoteSettingComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openMore(){
    const dialogRef = this.dialog.open(NoteSettingDialogComponent,{
      width: "25em",
      height: "7.5em"
    })

    dialogRef.afterClosed().subscribe(result => {
      console.log("More Note Options Dialog Box Closed")
    })
  }

}

@Component({
  selector: "app-note-setting-dialog",
  templateUrl: "note-setting-dialog.component.html"
})

export class NoteSettingDialogComponent {}

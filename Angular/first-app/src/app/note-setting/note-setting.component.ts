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

  openMore($event){
    console.log($event)
    let rect = $event.target.getBoundingClientRect()
    console.log(rect)
    let leftX = rect.x + 'px';
    let topY = rect.y + 'px';
    const dialogRef = this.dialog.open(NoteSettingDialogComponent,{
      width: "12.5em",
      height: "10.5em",
      position: {left: leftX, top: topY}
    })

    dialogRef.afterClosed().subscribe(result => {
      console.log("More Note Options Dialog Box Closed")
    })
  }

}

@Component({
  selector: "app-note-setting-dialog",
  templateUrl: "note-setting-dialog.component.html",
  styleUrls: ['./note-setting-dialog.component.css']
})

export class NoteSettingDialogComponent {

  showLabelsSignal

  constructor(){
    this.showLabelsSignal = false
  }

  showLabels(){
    if (this.showLabelsSignal === false){
      return this.showLabelsSignal = true;
    }
  }

}

import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { DataService } from '../services/DataService/data-service.service';

@Component({
  selector: 'app-note-setting',
  templateUrl: './note-setting.component.html',
  styleUrls: ['./note-setting.component.css']
})
export class NoteSettingComponent implements OnInit {

  @Output() sendLabels = new EventEmitter(false);

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
      // width: "12.5em",
      // height: "10.5em",
      position: {left: leftX, top: topY}
    })

    dialogRef.afterClosed().subscribe(result => {
      console.log(result)
      console.log("More Note Options Dialog Box Closed")
    })
  }

}


@Component({
  selector: "app-note-setting-dialog",
  templateUrl: "note-setting-dialog.component.html",
  styleUrls: ['./note-setting-dialog.component.css']
})

export class NoteSettingDialogComponent implements OnInit{

  showLabelsSignal:Boolean

  allLabels

  listOfLabels = []

  constructor(private dataService : DataService,
    public dialogRef: MatDialogRef<NoteSettingDialogComponent>){
    this.showLabelsSignal = false
  }

  ngOnInit(){
    this.dataService.labelData.subscribe(result => {
      this.allLabels = result;
      console.log(this.allLabels);
    })
  }

  showLabels(){
    if (this.showLabelsSignal === false){
      this.showLabelsSignal = true;
    }
  }

  toggle($event){
    console.log($event)
    if ($event.source.checked ===true){
      console.log($event.source.value);
      this.listOfLabels.push($event.source.value)
      console.log(this.listOfLabels)
    }
  }

  submitLabels(){
    this.dialogRef.close(this.listOfLabels)
  }

  onClose(){
    this.dialogRef.close();
  }
}

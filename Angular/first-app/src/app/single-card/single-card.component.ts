import { Component, OnInit, Input, Inject } from '@angular/core';
import { componentFactoryName } from '@angular/compiler';
import { MatDialog, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { inherits } from 'util';
import { not } from '@angular/compiler/src/output/output_ast';
import { DataService } from '../services/DataService/data-service.service';
import { type } from 'os';
import { HttpClientModule, HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-single-card',
  templateUrl: './single-card.component.html',
  styleUrls: ['./single-card.component.css']
})
export class SingleCardComponent implements OnInit {
  
  @Input() note;

  constructor(public dialog: MatDialog, private dataService : DataService) { 
  }

  ngOnInit(): void {
    console.log('note id: ', this.note.id ,'note_image : ' ,this.note.note_image)

  }

  showNoteDialog(){
    const dialogRef = this.dialog.open(SingleCardDialogComponent,{
      width: "45em",
      // height: "16.5em",
      data : this.note,
      panelClass : 'dialog-container',
      height: 'inherit',
      maxHeight: '30em',
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log("Note Dialog Box Closed");
    });
  } 

  setArchive($event){
    this.note.is_archived = $event;
    console.log('Crud Archive ---->  ',this.note.is_archived);
    console.log('Note Id ---> ',this.note.id);
    if (typeof(this.note.note_image) === 'string' || this.note.note_image === null){
      console.log('Note Image ----> ', this.note.note_image)
      delete this.note.note_image;
      console.log('Sending updated data to server');
      this.dataService.updateNote(this.note).subscribe(response => {
        console.log('response ----> ', response)
        if(response['success'] === true){
          // console.log('response ----> ', response)
          this.dataService.getAllNotes();
          this.dataService.getArchivedNotes();
        }; // Complete autoupdate here. 
      })
    }
  }

}

// SingleCardDialogComponent

@Component({
  selector: "app-single-card-component",
  templateUrl: "single-card-dialog.component.html",
  styleUrls: ['./single-card-dialog.component.css']
})

export class SingleCardDialogComponent {
  
  edited_date = new Date(this.data.last_edited).toDateString();

  constructor(
    public dialogRef: MatDialogRef<SingleCardDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data:any){}

    closeDialog(){
      this.dialogRef.close('Pizza')
    } 
}


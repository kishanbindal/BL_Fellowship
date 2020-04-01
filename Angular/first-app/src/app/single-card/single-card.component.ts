import { Component, OnInit, Input, Inject } from '@angular/core';
import { componentFactoryName } from '@angular/compiler';
import { MatDialog, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { inherits } from 'util';
import { not } from '@angular/compiler/src/output/output_ast';
import { DataService } from '../services/DataService/data-service.service';
import { type } from 'os';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';
import { DomSanitizer } from '@angular/platform-browser';
import { FormGroup, FormControl } from '@angular/forms';


@Component({
  selector: 'app-single-card',
  templateUrl: './single-card.component.html',
  styleUrls: ['./single-card.component.css']
})
export class SingleCardComponent implements OnInit {
  
  @Input() note;

  labels
  collaborators

  imgUrl;

  constructor(public dialog: MatDialog, private dataService : DataService,
    private _snackbar: MatSnackBar,
    private domSanitizer: DomSanitizer) { 
  }


  getLabelDetails(){
    // this.dataService.getLabels()
    this.dataService.labelData.subscribe(data => {
      this.labels = data
    })
    let labelObjs = []
    for (let labelId of this.note.labels){
      for (let label of this.labels){
        if (labelId == label.id){
          labelObjs.push(label)
        }
      }
    }
    this.note.labels = labelObjs
  }

  getCollaboratorDetails(){
    // this.dataService.getAllUsers()
    this.dataService.usersList.subscribe(data => {
      this.collaborators = data
    })
    setTimeout(()=> {
      let collab_objs = []
      // console.log('Coming from here')
      for (let collabId of this.note.collaborators){
        // console.log(collabId)
        for (let collab of this.collaborators){
          // console.log(collab)
          if (collab.pk === collabId){
            collab_objs.push(collab)
          }
        }
      }
      this.note.collaborators = collab_objs; 
    }, 200)
  }

  ngOnInit(): void {
    // console.log('note id: ', this.note.id ,'note_image : ' ,this.note.note_image)
    this.getLabelDetails()
    this.getCollaboratorDetails()

    if (this.note.note_image === null){
      this.imgUrl = undefined
    }
  }

  showNoteDialog(){
    const dialogRef = this.dialog.open(SingleCardDialogComponent,{
      width: "45em",
      // height: "16.5em",
      data : this.note,
      panelClass : 'dialog-container',
      // height: 'inherit',
      // maxHeight: '30em',
    });

    dialogRef.afterClosed().subscribe(data => {
      console.log('data from card dialog: ', data);
      this.dataService.updateNote(data).subscribe(response => {
        if(response['success'] === true ){
          this.dataService.getAllNotes()
          this.dataService.getArchivedNotes()
          this.dataService.getReminderNotes()
        }
        else{
          this._snackbar.open('Unable to Update Note, Please try again', 'close', {
            duration: 3000
          })
        }
      })
    });
  } 

  // setArchive($event){
  //   this.note.is_archived = $event;
  //   console.log('Crud Archive ---->  ',this.note.is_archived);
  //   console.log('Note Id ---> ',this.note.id);
  //   if (typeof(this.note.note_image) === 'string' || this.note.note_image === null){
  //     console.log('Note Image ----> ', this.note.note_image)
  //     // delete this.note.note_image;
  //     console.log('Sending updated data to server');
  //     this.dataService.updateNote(this.note).subscribe(response => {
  //       console.log('response ----> ', response)
  //       if(response['success'] === true){
  //         // console.log('response ----> ', response)
  //         this.dataService.getAllNotes();
  //         this.dataService.getArchivedNotes();
  //       }; // Complete autoupdate here. 
  //     })
  //   }
  // }

  setArchive($event){
    this.note.is_archived = $event;
    let data = {'id': this.note.id, 'is_archived': this.note.is_archived}
    this.dataService.updateNote(data).subscribe(response => {
      if (response['success'] === true && this.note.is_archived === true){
        this._snackbar.open('Note has been archived', 'Close', {
          duration : 3000
        })
      }else{
        this._snackbar.open('Note has been Unarchived', 'Close', {
          duration : 3000
        })
      }
      this.dataService.getAllNotes();
      this.dataService.getArchivedNotes();
    })
  }

  setColor($event){
    this.note.color = $event;
    let data = {'id':this.note.id,'color': this.note.color}
    this.dataService.updateNote(data). subscribe(response => {
      if (response['success'] === false){
        this._snackbar.open('Unable to Set Color', 'Close',{
          duration: 1500
        })
      }
    })
  }

  setCollaborators($event){
    console.log('Collab Event : ',$event)
    this.note.collaborators = $event
    let collabIds = []
    for (let collab of this.note.collaborators){
      collabIds.push(collab.pk)
    }
    // console.log('Collab data to backend : ', collabIds)
    let data = {'id': this.note.id, 'collaborators': collabIds};
    this.dataService.updateNote(data).subscribe(response => {
      if (response['success'] === false){
        this._snackbar.open('Unable to Set Collaborator. Please try again.', 'Close', {
          duration: 2000
        })
      }
    })
  }

  setImage($event){
    // console.log('Image Event : ',$event)
    this.imgUrl= $event[1]
    this.imgUrl = this.domSanitizer.bypassSecurityTrustUrl(this.imgUrl)

    let otherData = {
      'id': this.note.id
    }
    let formData = new FormData();
    formData.append('note_image', $event[0]);
    formData.append('id', this.note.id);
    this.dataService.updateNote(formData).subscribe(response =>{
      if (response['success'] === true){
        this.dataService.getAllNotes()
      }else{
        this._snackbar.open('Unable to Add image, Please try again', 'close', {
          duration: 3000
        })
      }
    })
  }

  setReminder($event){
    // console.log('Reminder Event :', $event)
    let reminder  = new Date($event)
    let date =  reminder.getFullYear()+'-'+(reminder.getMonth()+1)+'-'+reminder.getDate();
    let time = reminder.getHours()+':'+reminder.getMinutes()+':'+reminder.getSeconds();
    let finalReminder = date + ' ' + time 
    console.log('reminder event recorded  :', finalReminder);
    this.note.reminder = finalReminder;

    let data = {'id': this.note.id, 'reminder': finalReminder}
    this.dataService.updateNote(data).subscribe(response => {
      if (response['success'] === false){
        this._snackbar.open('Unable to add reminder, Please try again.', 'close', {duration:3000})
      }
    })
  }

  setLabels($event){
    console.log('Labels Event:',$event)
    this.note.labels = $event
    let labelsId =[]
    for (let label of $event){
      labelsId.push(label.id)
    }
    let data = {'id': this.note.id, 'labels': labelsId}; console.log('note label data to backend :',labelsId);
    this.dataService.updateNote(data).subscribe(response => {
      if (response['success']===false){
        this._snackbar.open('Unable to add Labels, Please try again', 'close', {duration: 3000})
      }
    })
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

  title= new FormControl(this.data.title);
  note_text= new FormControl(this.data.note_text)
  imgUrl;

  constructor(
    public dialogRef: MatDialogRef<SingleCardDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data:any,
    private dataService : DataService,
    private _snackbar : MatSnackBar,
    public domSanitizer: DomSanitizer){}

    closeDialog(){
      let text_data = {'id': this.data.id, 'title': this.title.value,'note_text': this.note_text.value}
      this.dialogRef.close(text_data)
    } 

    setArchive($event){
      this.data.is_archived = $event;
      let sendData = {'id': this.data.id, 'is_archived': this.data.is_archived}
      console.log('Data :', sendData)
      this.dataService.updateNote(sendData).subscribe(response => {
        if (response['success'] === true && this.data.is_archived === true){
          this._snackbar.open('Note has been archived', 'Close', {
            duration : 3000
          })
          this.dialogRef.close()
        }else{
          this._snackbar.open('Note has been Unarchived', 'Close', {
            duration : 3000
          })
        }
        this.dataService.getAllNotes();
        this.dataService.getArchivedNotes();
      })
    }

    setReminder($event){
      // console.log('Reminder Event :', $event)
      let reminder  = new Date($event)
      let date =  reminder.getFullYear()+'-'+(reminder.getMonth()+1)+'-'+reminder.getDate();
      let time = reminder.getHours()+':'+reminder.getMinutes()+':'+reminder.getSeconds();
      let finalReminder = date + ' ' + time 
      console.log('reminder event recorded  :', finalReminder);
      this.data.reminder = finalReminder;
  
      let data = {'id': this.data.id, 'reminder': finalReminder}
      this.dataService.updateNote(data).subscribe(response => {
        if (response['success'] === false){
          this._snackbar.open('Unable to add reminder, Please try again.', 'close', {duration:3000})
        }
      })
    }

  
    setCollaborators($event){
      console.log('Collab Event : ',$event)
      this.data.collaborators = $event
      let collabIds = []
      for (let collab of this.data.collaborators){
        collabIds.push(collab.pk)
      }
      // console.log('Collab data to backend : ', collabIds)
      let data = {'id': this.data.id, 'collaborators': collabIds};
      this.dataService.updateNote(data).subscribe(response => {
        if (response['success'] === false){
          this._snackbar.open('Unable to Set Collaborator. Please try again.', 'Close', {
            duration: 2000
          })
        }
      })
    }

    setColor($event){
      this.data.color = $event;
      let data = {'id':this.data.id,'color': this.data.color}
      this.dataService.updateNote(data). subscribe(response => {
        if (response['success'] === false){
          this._snackbar.open('Unable to Set Color', 'Close',{
            duration: 1500
          })
        }
      })
    }

    setImage($event){
      // console.log('Image Event : ',$event)
      this.imgUrl= $event[1]
      this.imgUrl = this.domSanitizer.bypassSecurityTrustUrl(this.imgUrl)
  
      let otherData = {
        'id': this.data.id
      }
      let formData = new FormData();
      formData.append('note_image', $event[0]);
      formData.append('id', this.data.id);
      this.dataService.updateNote(formData).subscribe(response =>{
        if (response['success'] === true){
          this.dataService.getAllNotes()
        }else{
          this._snackbar.open('Unable to Add image, Please try again', 'close', {
            duration: 3000
          })
        }
      })
    }

    setLabels($event){
      console.log('Labels Event:',$event)
      this.data.labels = $event
      let labelsId =[]
      for (let label of $event){
        labelsId.push(label.id)
      }
      let data = {'id': this.data.id, 'labels': labelsId}; console.log('note label data to backend :',labelsId);
      this.dataService.updateNote(data).subscribe(response => {
        if (response['success']===false){
          this._snackbar.open('Unable to add Labels, Please try again', 'close', {duration: 3000})
        }
      })
    }

}


import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-add-note',
  templateUrl: './add-note.component.html',
  styleUrls: ['./add-note.component.css']
})
export class AddNoteComponent implements OnInit {

  showCard: boolean;

  templateNote: {
    collaborators: Array<string>,
    color: string,
    created_on: string,
    is_archived: boolean,
    is_pinned: boolean,
    is_trashed: boolean,
    labels: Array<string>,
    last_edited: string,
    link: string,
    note_image: File,
    note_text: string,
    reminder: string,
    title: string,
  }

  constructor(public noteService : DataService, private _snackbar: MatSnackBar) {
    this.showCard = false;
  }

  ngOnInit(): void {
    this.templateNote = {
      collaborators:[],
      color: "",
      created_on: "",
      is_archived: false,
      is_pinned: false,
      is_trashed: false,
      labels: [],
      last_edited: "",
      link: "",
      note_image: null,
      note_text: "",
      reminder: null,
      title: "",
    }
  }

  openCard(){
    if (this.showCard === false){
      return this.showCard = true
    }
  }
  
  private SendNoteData(note_data:object){
    if (this.templateNote.title !== '' || this.templateNote.note_text !== ''){
      this.noteService.postNote(note_data).subscribe((result) => {
        if (result['success'] == true){
          this.noteService.getAllNotes();
          this._snackbar.open('Successfully Created Note',"close",{
            duration: 2000,
          } 
        )
        }else{
          console.log('Error')
        }
        
      })
    }
  }

  closeCard(){
    if(this.showCard === true){
      this.showCard = false;
      console.log(`Note title : ${this.templateNote.title}\nNote Text : ${this.templateNote.note_text}`);
      this.SendNoteData(this.templateNote)
      return this.showCard
    }
  }

  setColor($event){
    console.log('Event Recorded')
    this.templateNote.color = $event;
  }

  // doSomething(){
  //   console.log('Got your event')
  // }

}
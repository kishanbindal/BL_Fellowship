import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { DomSanitizer } from '@angular/platform-browser'

@Component({
  selector: 'app-add-note',
  templateUrl: './add-note.component.html',
  styleUrls: ['./add-note.component.css']
})
export class AddNoteComponent implements OnInit {

  showCard: boolean;

  templateNote: {
    collaborators,//: Array<string>,
    color: string,
    // created_on: string,
    is_archived: boolean,
    is_pinned: boolean,
    is_trashed: boolean,
    labels,//: Array<string>,
    link: string,
    note_image,
    note_text: string,
    reminder: string,
    title: string,
  }

  formData = new FormData();
  imgFile = null;
  imgData:File;

  constructor(public noteService : DataService, private _snackbar: MatSnackBar,
    private domSanitizer : DomSanitizer) {
    this.showCard = false;
  }

  ngOnInit(): void {

    this.templateNote = {
      collaborators:[],
      color: "",
      is_archived: false,
      is_pinned: false,
      is_trashed: false,
      labels: [],
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

  // convertToFormData(note_data:object, img_data:File){
  //   // for (var content in this.templateNote){
  //   //     this.formData.append(content, this.templateNote[content]);
  //   // }
  //   let otherData = JSON.stringify(note_data);
  //   this.formData.append('note_image', img_data, img_data.name)
  //   this.formData.append('note_data', otherData)
  // }
  
  private SendNoteData(note_data){

    const data={
      color: this.templateNote.color,
      is_archived: this.templateNote.is_archived,
      is_pinned: false,
      is_trashed: false,
      labels: this.templateNote.labels,
      collaborators: this.templateNote.collaborators,
      reminder: this.templateNote.reminder,
      note_text: this.templateNote.note_text,
      title: this.templateNote.title,
    }


    const otherData=JSON.stringify(data)
    const formData = new FormData();
    if (this.imgData !== undefined){
      formData.append('note_image',this.imgData) //this.imgData.name
    }
    formData.append('otherData',otherData)
    
    if (this.templateNote.title !== '' || this.templateNote.note_text !== ''){
      this.noteService.postNote(formData).subscribe(result => {
        
        console.log(result,'---->result')

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
      // this.convertToFormData(this.templateNote, this.imgData);
      this.SendNoteData(this.formData)
      return this.showCard
    }
  }

  setColor($event){
    console.log('Setting Color')
    this.templateNote.color = $event;
  }

  setReminder($event){
    let reminder  = new Date($event)
    let date =  reminder.getFullYear()+'-'+(reminder.getMonth()+1)+'-'+reminder.getDate();
    let time = reminder.getHours()+':'+reminder.getMinutes()+':'+reminder.getSeconds();
    let finalReminder = date + ' ' + time 
    console.log('reminder event recorded  :', finalReminder);
    this.templateNote.reminder = finalReminder;
  }

  setImage($event){
    // this.templateNote.note_image = $event[0];
    this.imgData=$event[0];
    // this.fd.append('note_image', $event[0], $event[0].name)
    // this.templateNote.note_image = this.fd
    let imgUrl = $event[1];
    this.imgFile = this.domSanitizer.bypassSecurityTrustUrl(imgUrl)
    console.log(' Note Template : \n',this.templateNote)
  }

  setArchive($event){
    console.log($event)
    this.templateNote.is_archived = $event;
  }

  setLabels($event){
    console.log($event)
   this.templateNote.labels = $event
  }

  setCollaborators($event){
    for (let obj of $event){
      console.log('Object in add note component\ : \n', obj)
      this.templateNote.collaborators.push(obj.pk)
    }
    console.log('Final Collab List :', this.templateNote.collaborators)
  }

}
